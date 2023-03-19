from ..models import Chat


def get_chat(chatId: int) -> Chat or None:
    return Chat.get_or_none(Chat.chatId == chatId)

def create_or_update_chat(chatId, facultyId, courseId, groupId) -> Chat:
    timetable = get_chat(chatId)
    if timetable:
        timetable.facultyId = facultyId
        timetable.courseId = courseId
        timetable.groupId = groupId
        timetable.save()
    else:
        timetable = Chat.create(chatId=chatId, facultyId=facultyId, courseId=courseId, groupId=groupId)
    return timetable