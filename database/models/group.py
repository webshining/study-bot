from pydantic import Field

from .base import Base


class Group(Base):
    id: int = Field(alias="_id", default_factory=int)
    name: str


Group.set_collection("groups")
