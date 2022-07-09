from account.models import MyUser as User
from shop.models import Product, Comment
from config.db import postgres_db

postgres_db.bind([User, Product, Comment])
postgres_db.create_tables([User, Product, Comment])
postgres_db.close()