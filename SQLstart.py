import pymysql
from pymysql.cursors import DictCursor


class DataBase:
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

    def addUser(self, login, password):
        sql = "INSERT INTO users (id, login, password) VALUES (%s, %s, %s)"
        temp = ["NULL", login, password]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def getUser(self):
        sql = "SELECT *FROM users"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        print(data)

    def getLogin(self):
        sql = "SELECT login FROM users "
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data




#qwer.addUser('Art.by','23456')

def input_log():
    read = DataBase()
    #print(read.getLogin())
    lst = read.getLogin()
    del read
    print(lst)
    log= input("Введите логин ")

    for el in lst:
        if log == el["login"]:
            return log
            break
    return None




def input_password():
    pas= input("Введите пароль ")
    if len(pas) < 6:
        print('Пароль должен быть не менее 6 символов, попробуйте еще раз')
    else:
        return pas


def shifr(pas):
    home=pas[0]
    end = pas[-1]
    new_pas = pas.replace(home,end,1)
    new_pas=new_pas[0:-1]+home
    return new_pas

print(input_log())
'''while True:
    pas = input_password()
    if pas != None:
        print(shifr(pas))
        break'''









