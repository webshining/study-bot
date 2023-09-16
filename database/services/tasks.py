from datetime import date

from utils import week_start_end
from ..models import Task, User


def get_task(id: int) -> Task | None:
    task = Task.get_or_none(Task.id == id)
    return task


def get_tasks(group_id: int = None, date_range: [date] = None, status: str = None) -> [Task]:
    tasks = Task.select()
    if group_id:
        tasks = tasks.where(Task.group_id == group_id)
    if date_range:
        tasks = tasks.where((Task.date >= date_range[0]) & (Task.date <= date_range[1]))
    if status is not None:
        tasks = tasks.where(Task.status == status)
    return list(tasks)


def create_task(name: str, text: str, _date: date, group_id: int, creator: User, confirmed: bool = False) -> Task:
    return Task.create(name=name, text=text, date=_date, group_id=group_id, confirmed=confirmed, creator=creator)


def delete_task(id: int):
    return Task.delete_by_id(id)
