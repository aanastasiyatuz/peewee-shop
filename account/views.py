from .models import MyUser as User

def register():
    username = input("Введите username: ")
    password = input("Введите пароль: ")
    User.create(username=username, password=password)
    return "Юзер успешно зарегистрирован"

