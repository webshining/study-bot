import json
from datetime import date, datetime, time

import aiohttp
from fake_useragent import UserAgent
from pydantic import BaseModel, Field, StrictStr, validator

from data.config import DIR

from .logging import logger
from .time import get_current_time, week_start_end


def headers():
    return {"Accept-Language": "uk", 'User-Agent': UserAgent().random}

def save_to_file(filename: str, data: object):
    json.dump(data, open(f'{DIR}/save/{filename}', "w", encoding="utf-8"), indent=4, ensure_ascii=False)


def read_file(filename: str) -> any or None:
    try:
        return json.load(open(f'{DIR}/save/{filename}'))
    except:
        return None


class Group(BaseModel):
    id: int
    name: str


class Faculty(BaseModel):
    id: int
    name: str = Field(alias='fullName')


class Course(BaseModel):
    id: int = Field(alias='course')
    name: StrictStr = Field(alias='course')

    @validator('name', pre=True)
    def parse_time(cls, v):
        return str(v)


class Period(BaseModel):
    disciplineFullName: str
    classroom: str
    timeStart: datetime
    timeEnd: datetime
    teachersName: str
    type: str = Field(alias="typeStr")

    @validator('timeStart', 'timeEnd', pre=True)
    def parse_time(cls, v):
        return datetime.combine(get_current_time().date(), datetime.strptime(v, "%H:%M").time())


class Lesson(BaseModel):
    number: int
    periods: list[Period]


class Day(BaseModel):
    date: date
    lessons: list[Lesson]

    @validator('date', pre=True)
    def parse_date(cls, v):
        return datetime.strptime(v, "%Y-%m-%d").date()


class Call(BaseModel):
    timeStart: time
    timeEnd: time

    @validator('timeStart', 'timeEnd', pre=True)
    def parse_time(cls, v):
        return datetime.strptime(v, "%H:%M").time()


async def get_faculties() -> list[Faculty] or None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post('https://mia.mobil.knute.edu.ua/list/faculties', 
                                    headers=headers(), timeout=1.5) as res:
                faculties = [Faculty(**i) for i in await res.json()]
                save_to_file('faculties.json', await res.json())
                return faculties
    except Exception as e:
        logger.error(e)
        data = read_file('faculties.json')
        return [Faculty(**i) for i in data] if data else data


async def get_courses(facultyId: int) -> list[Course] or None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post('https://mia.mobil.knute.edu.ua/list/courses', 
                                    data={"facultyId": facultyId}, 
                                    headers=headers(), timeout=1.5) as res:
                courses = [Course(**i) for i in await res.json()]
                save_to_file('courses.json', await res.json())
                return courses
    except Exception as e:
        logger.error(e)
        data = read_file('courses.json')
        return [Course(**i) for i in data] if data else data


async def get_groups(facultyId: int, courseId: int) -> list[Group] or None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post('https://mia.mobil.knute.edu.ua/list/groups', 
                                    data={"facultyId": facultyId, "course": courseId}, 
                                    headers=headers(), timeout=1.5) as res:
                groups = sorted([Group(**i) for i in await res.json()], key=lambda g: g.name)
                save_to_file('groups.json', await res.json())
                return groups
    except Exception as e:
        logger.error(e)
        data = read_file('courses.json')
        return sorted([Group(**i) for i in data], key=lambda g: g.name) if data else data


async def get_schedule(groupId: int, date_range: list[date] = None) -> list[Day] or None:
    date_range = date_range if date_range else week_start_end()
    try:
        date_start, date_end = [i.strftime("%Y-%m-%d") for i in date_range]
        async with aiohttp.ClientSession() as session:
            async with session.post('https://mia.mobil.knute.edu.ua/time-table/group', 
                                    data={"groupId": groupId, "dateStart": date_start, "dateEnd": date_end}, 
                                    headers=headers(), timeout=1.5) as res:
                timetable = [Day(**i) for i in await res.json() if
                            [l for l in i['lessons'] if [p for p in l['periods'] if p['timeStart']]]]
                save_to_file(f'{groupId}.json', await res.json())
                return timetable
    except Exception as e:
        logger.error(e)
        data = read_file(f'{groupId}.json')
        return [Day(**i) for i in data if
                [l for l in i['lessons'] if [p for p in l['periods'] if p['timeStart']]]] if data else data


async def get_timetable_call() -> list[Call] or None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post('https://mia.mobil.knute.edu.ua/time-table/call-schedule', 
                                    headers=headers(), timeout=1.5) as res:
                save_to_file('call.json', await res.json())
                return [Call(**i) for i in await res.json()]
    except Exception as e:
        logger.error(e)
        data = read_file('call.json')
        return [Call(**i) for i in data] if data else data
