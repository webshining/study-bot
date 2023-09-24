from pydantic import BaseModel


class UserPatch(BaseModel):
    status: str
