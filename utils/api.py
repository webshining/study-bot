import json
import requests
from datetime import datetime, date, time
from pydantic import BaseModel, validator
from .time import week_start_end

class Faculty(BaseModel):
    id: int
    shortName: str
    fullName: str

class Course(BaseModel):
    course: int

class Group(BaseModel):
    id: int
    name: str
    
class Period(BaseModel):
    disciplineFullName: str
    classroom: str
    timeStart: time
    timeEnd: time
    teachersName: str
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

def get_faculties() -> list[Faculty]:
    r = requests.post('https://mia.mobil.knute.edu.ua/list/faculties', {"structureId": 0}, headers={"Accept-Language": "uk-UA,uk;"})
    return [Faculty(**i) for i in json.loads(r.text)]

def get_courses(facultyId: int) -> list[Course]:
    r = requests.post('https://mia.mobil.knute.edu.ua/list/courses', {"facultyId": facultyId}, headers={"Accept-Language": "uk-UA,uk;"})
    return [Course(**i) for i in json.loads(r.text)]

def get_groups(facultyId: int, courseId: int) -> list[Group]:
    r = requests.post('https://mia.mobil.knute.edu.ua/list/groups', {"facultyId": facultyId, "course": courseId}, headers={"Accept-Language": "uk-UA,uk;"})
    return [Group(**i) for i in json.loads(r.text)]


def get_timetable(groupId: int, dateRange: list[date] = week_start_end()) -> list[Day]:
    dateStart = dateRange[0].strftime("%Y-%m-%d")
    dateEnd = dateRange[1].strftime("%Y-%m-%d")
    r = requests.post('https://mia.mobil.knute.edu.ua/time-table/group', {"groupId": groupId, "dateStart": dateStart, "dateEnd": dateEnd}, headers={"Accept-Language": "uk-UA,uk;"})
    return [Day(**i) for i in json.loads(r.text)]