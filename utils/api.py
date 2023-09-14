import json
from datetime import date, datetime, time

import requests
from pydantic import BaseModel, Field, StrictStr, validator

from data.config import DIR

from .logging import logger
from .time import get_current_time, week_start_end


def save_to_file(filename: str, data: object):
    json.dump(data, open(f'{DIR}/data/{filename}', "w"), indent=4, ensure_ascii=False)
    
def read_file(filename: str) -> any or None:
    try:
        return json.load(open(f'{DIR}/data/{filename}'))
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
    
def get_faculties() -> list[Faculty] or None:
    try:
        r = requests.post('https://mia.mobil.knute.edu.ua/list/faculties', {"structureId": 0}, headers={"Accept-Language": "uk-UA,uk;"})
        faculties = [Faculty(**i) for i in json.loads(r.text)]
        save_to_file('faculties.json', json.loads(r.text))
        return faculties
    except Exception as e:
        logger.error(e)
        data = read_file('faculties.json')
        return [Faculty(**i) for i in data] if data else data

def get_courses(facultyId: int) -> list[Course] or None:
    try:
        r = requests.post('https://mia.mobil.knute.edu.ua/list/courses', {"facultyId": facultyId}, headers={"Accept-Language": "uk-UA,uk;"})
        courses = [Course(**i) for i in json.loads(r.text)]
        save_to_file('courses.json', json.loads(r.text))
        return courses
    except Exception as e:
        logger.error(e)
        data = read_file('courses.json')
        return [Course(**i) for i in data] if data else data

def get_groups(facultyId: int, courseId: int) -> list[Group] or None:
    try:
        r = requests.post('https://mia.mobil.knute.edu.ua/list/groups', {"facultyId": facultyId, "course": courseId}, headers={"Accept-Language": "uk-UA,uk;"})
        groups = sorted([Group(**i) for i in json.loads(r.text)], key=lambda g: g.name)
        save_to_file('groups.json', json.loads(r.text))
        return groups
    except Exception as e:
        logger.error(e)
        data = read_file('courses.json')
        return sorted([Group(**i) for i in data], key=lambda g: g.name) if data else data

def get_timetable(groupId: int, dateRange: list[date] = week_start_end()) -> list[Day] or None:
    try:
        dateStart = dateRange[0].strftime("%Y-%m-%d")
        dateEnd = dateRange[1].strftime("%Y-%m-%d")
        r = requests.post('https://mia.mobil.knute.edu.ua/time-table/group', {"groupId": groupId, "dateStart": dateStart, "dateEnd": dateEnd}, headers={"Accept-Language": "uk-UA,uk;"})
        timetable = [Day(**i) for i in json.loads(r.text) if [l for l in i['lessons'] if [p for p in l['periods'] if p['timeStart']]]]
        save_to_file(f'{groupId}.json', json.loads(r.text))
        return timetable
    except Exception as e:
        logger.error(e)
        data = read_file(f'{groupId}.json')
        return [Day(**i) for i in data if [l for l in i['lessons'] if [p for p in l['periods'] if p['timeStart']]]] if data else data

def get_timetable_call() -> list[Call] or None:
    try:
        r = requests.post('https://mia.mobil.knute.edu.ua/time-table/call-schedule')
        save_to_file('call.json', json.loads(r.text))
        return [Call(**i) for i in json.loads(r.text)]
    except Exception as e:
        logger.error(e)
        data = read_file('call.json')
        return [Call(**i) for i in data] if data else data