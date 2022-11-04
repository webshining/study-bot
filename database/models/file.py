from pydantic import BaseModel


class File(BaseModel):
    name: str
    file_id: str
