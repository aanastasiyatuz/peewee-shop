import peewee
from db import postgres_db

class BaseModel(peewee.Model):
    class Meta:
        database = postgres_db
