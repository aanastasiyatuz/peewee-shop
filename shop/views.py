from .models import Product, Comment
from account.models import MyUser as User
from .serializers import ProductSerializer


def create_product():
    category = input("Введите категорию продукта: ")
    title = input("Введите название продукта: ")
    price = float(input("Введите цену продукта: "))
    description = input("Введите описание продукта:\n")
    Product.create(category=category, title=title, price=price, description=description)
    return "Продукт успешно создан"

def product_list():
    return ProductSerializer().serialize_queryset()

def product_detail(p_id):
    product = Product.get(id=p_id)
    return ProductSerializer().serialize_obj(product)

def product_update(p_id):
    product = Product.get(id=p_id)
    field = input("Введите поле для изменения: ")
    if field in dir(product):
        val = input(f"{field} = ")
        setattr(product, field, val)
        product.save()
        return "Продукт успешно изменен"
    return "Такого поля нет"

def create_comment(p_id):
    from datetime import datetime
    username = input("Введите username: ")
    user = User.get(username=username)
    product = Product.get(id=p_id)
    body = input("Введите комментарий:\n")
    Comment.create(user=user, product=product, body=body, created_at=datetime.now())
    return "Комментарий успешно создан"
