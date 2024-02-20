from bson.objectid import ObjectId as BsonObjectId
from motor.motor_tornado import MotorCollection
from pydantic import BaseModel

from loader import db


class ObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError('ObjectId required')
        return str(v)


class Base(BaseModel):
    _collection: MotorCollection = None

    @classmethod
    async def count(cls):
        num = await cls._collection.count_documents({})
        return num

    @classmethod
    async def get(cls, id: int):
        obj = await cls._collection.find_one({'_id': id})
        return cls(**obj) if obj else None

    @classmethod
    async def get_by(cls, **kwargs):
        obj = await cls._collection.find_one(kwargs)
        return cls(**obj) if obj else None

    @classmethod
    async def get_all(cls, **kwargs):
        objs = await cls._collection.find(kwargs).to_list(1000)
        return [cls(**o) for o in objs]

    @classmethod
    async def update(cls, id: int, **kwargs):
        await cls._collection.find_one_and_update({'_id': id}, {'$set': kwargs})
        return await cls.get(id)

    @classmethod
    async def nextid(cls):
        element = await cls._collection.find().sort({"_id": -1}).limit(1).to_list(1)
        element = next(iter(element), None)
        return element['_id'] + 1 if element else 1

    @classmethod
    async def create(cls, **kwargs):
        if 'id' in kwargs:
            kwargs['_id'] = kwargs.pop('id')
        elif '_id' not in kwargs:
            kwargs["_id"] = await cls.nextid()
        obj = cls(**kwargs)
        await cls._collection.insert_one(obj.model_dump(by_alias=True))
        return obj

    @classmethod
    async def delete(cls, filter):
        await cls._collection.delete_many(filter)
        return True

    @classmethod
    def set_collection(cls, collection: str):
        cls._collection = db[collection]
