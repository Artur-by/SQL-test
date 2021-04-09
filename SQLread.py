

class User:
    def __init__(self, login, password,name):
        self.login = login
        self.password = password
        self.name = name

    def __str__(self):
        return f'пользователь :логин:{self.login}, пароль:{self.password}, имя:{self.name}'



def matter(id):
