from pydantic import BaseModel


class File(BaseModel):
    file_id: str
    name: str
