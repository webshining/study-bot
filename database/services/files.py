from ..models import File


def create_file(file_id: str, file_type: str, task_id: int) -> File:
    return File.create(file_id=file_id, file_type=file_type, task=task_id)
