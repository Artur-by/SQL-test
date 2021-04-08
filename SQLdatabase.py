import pymysql
from pymysql.cursors import DictCursor


class DataBase:                     # класс работы с SQL
    def __init__(self):
        self.connection = self.connect()
        self.cursors = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def connect(self):
        connection = pymysql.connect(
            host='localhost',
            user='admin',
            password='qwerty123',
            db='overone',
            charset='utf8mb4',
            cursorclass=DictCursor
        )
        return connection

    def addUser(self, login, password):                              # метод записи логина и пароля пользователя
        sql = "INSERT INTO users (id, login, password) VALUES (%s, %s, %s)"
        temp = ["NULL", login, password]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def addFullUser(self, ID, name, lastname, faculty, type, theme):  # метод записи данных пользователя
        sql = "INSERT INTO full_users (ID, name, lastname, faculty, type, theme) VALUES (%s, %s, %s, %s, %s, %s)"
        temp = [ID, name, lastname, faculty, type, theme]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def getFullUser(self, id):                                              # метод запроса логина и пароля
        sql = f"SELECT * FROM full_users WHERE ID={id}"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data

    def getLogin(self):                                                # метод запроса логина и пароля
        sql = "SELECT ID, login, password FROM users "
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data

    def getPassword(self):                                              # метод запроса  пароля
        sql = "SELECT password FROM users "
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data

    def getId(self, log):                                               # метод запроса ID
        sql = f"SELECT ID FROM users WHERE login = '{log}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data



def record_lpas(log,pas):                                                # функция записи логина и пароля
    lpas = DataBase()
    lpas.addUser(log,pas)
    lpas.getLogin()
    del lpas

def record_fullus(ID, name, lastname, faculty, type, theme):            # функция записи данных пользователя
    fullus = DataBase()
    fullus.addFullUser(ID, name, lastname, faculty, type, theme)
    del fullus

def read_id(log):                                                       # функция запрашивает ID и возвращает число
    logid = DataBase()
    lstid= logid.getId(log)
    #for el in lstid:
    #   idnew = el["ID"]
    return lstid[0]['ID']


def input_log(log1):            # функция ввода логина и проверки на наличие в базе
    read = DataBase()
    lst = read.getLogin()
    del read
    log= log1

    for el in lst:
        if log == el["login"]:
            pas = el["password"]
            id = el["ID"]
            return id, log, pas
            break
    return None


def input_password():                   # функция ввода  пароля не менее 5 символов
    read = DataBase()
    lst = read.getPassword()
    del read



    pas= input("Введите пароль ")
    if len(pas) < 5:
        print('Пароль должен быть не менее 5 символов, попробуйте еще раз')
    else:
        for el in lst:
            if pas == el["password"]:
                return pas
                break

        return None

        return pas



def shifr_password():                       # функция шифрования пароля, меняем первый и последний элемент местами
    while True:
        pas = input("Введите пароль ")
        if len(pas) < 5:
            print('Пароль должен быть не менее 5 символов, попробуйте еще раз')
        else:
            home=pas[0]
            end = pas[-1]
            new_pas = pas.replace(home,end,1)
            new_pas=new_pas[0:-1]+home
            return new_pas
            break



