import json
from datetime import date, datetime, time

import requests
from pydantic import BaseModel, Field, StrictStr, validator

from .time import week_start_end


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
    timeStart: time
    timeEnd: time
    teachersName: str

    @validator('timeStart', 'timeEnd', pre=True)
    def parse_time(cls, v):
        return datetime.strptime(v, "%H:%M").time()

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
    
def get_faculties() -> list[Faculty]:
    r = requests.post('https://mia.mobil.knute.edu.ua/list/faculties', {"structureId": 0}, headers={"Accept-Language": "uk-UA,uk;"})
    return [Faculty(**i) for i in json.loads(r.text)]

def get_courses(facultyId: int) -> list[Course]:
    r = requests.post('https://mia.mobil.knute.edu.ua/list/courses', {"facultyId": facultyId}, headers={"Accept-Language": "uk-UA,uk;"})
    return [Course(**i) for i in json.loads(r.text)]

def get_groups(facultyId: int, courseId: int) -> list[Group]:
    r = requests.post('https://mia.mobil.knute.edu.ua/list/groups', {"facultyId": facultyId, "course": courseId}, headers={"Accept-Language": "uk-UA,uk;"})
    return sorted([Group(**i) for i in json.loads(r.text)], key=lambda g: g.name)

def get_timetable(groupId: int, dateRange: list[date] = week_start_end()) -> list[Day]:
    dateStart = dateRange[0].strftime("%Y-%m-%d")
    dateEnd = dateRange[1].strftime("%Y-%m-%d")
    r = requests.post('https://mia.mobil.knute.edu.ua/time-table/group', {"groupId": groupId, "dateStart": dateStart, "dateEnd": dateEnd}, headers={"Accept-Language": "uk-UA,uk;"})
    return [Day(**i) for i in json.loads(r.text) if [l for l in i['lessons'] if [p for p in l['periods'] if p['timeStart']]]]

def get_timetable_call() -> list[Call]:
    r = requests.post('https://mia.mobil.knute.edu.ua/time-table/call-schedule')
    return [Call(**i) for i in json.loads(r.text)]