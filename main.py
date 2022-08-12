from peewee import JOIN

from loader import database
from database import User, Subject, Day, init_week, DaySubjectThrough, File


if __name__ == '__main__':
    # database.create_tables([User, Subject, Day, DaySubjectThrough, File])
    # init_week()
    print(list(Day.select(Day, DaySubjectThrough.subject_number)
                  .join(DaySubjectThrough, JOIN.LEFT_OUTER)
                  .order_by(DaySubjectThrough.subject_number)))
