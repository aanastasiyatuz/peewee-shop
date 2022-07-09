import peewee
from config.db import postgres_db

class BaseModel(peewee.Model):
    class Meta:
        database = postgres_db
