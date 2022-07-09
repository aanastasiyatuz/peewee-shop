from peewee import PostgresqlDatabase
from decouple import config

postgres_db = PostgresqlDatabase(
    "peewee_shop", 
    user=config('db_user'), 
    password=config('db_password'), 
    host='127.0.0.1', 
    port=5432
    )

