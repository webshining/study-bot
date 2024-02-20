from pydantic import Field

from .base import Base


class User(Base):
    id: int = Field(alias="_id", default_factory=int)
    name: str
    username: str | None = Field(None)
    status: str = Field("user")
    group: int | None = Field(None)

    def is_admin(self):
        return self.status == "admin"

    @classmethod
    async def get_or_create(cls, id: int, name: str, username: str = None):
        if await cls.get(id):
            user = await cls.update(id, name=name, username=username)
        else:
            user = await cls.create(id=id, name=name, username=username, group=None)
        return user


User.set_collection("users")
