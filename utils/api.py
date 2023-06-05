import json
from datetime import date, datetime, time

import requests
from pydantic import BaseModel, validator

from .time import week_start_end


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

def get_timetable(dateRange: list[date] = week_start_end()) -> list[Day]:
    dateStart = dateRange[0].strftime("%Y-%m-%d")
    dateEnd = dateRange[1].strftime("%Y-%m-%d")
    r = requests.post('https://mia.mobil.knute.edu.ua/time-table/group', {"groupId": 1009, "dateStart": dateStart, "dateEnd": dateEnd}, headers={"Accept-Language": "uk-UA,uk;"})
    return [Day(**i) for i in json.loads(r.text)]

def get_timetable_call() -> list[Call]:
    r = requests.post('https://mia.mobil.knute.edu.ua/time-table/call-schedule')
    return [Call(**i) for i in json.loads(r.text)]