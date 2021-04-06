""" Создать базу данных для преподавателей и студентов, с возможностью добавления, просмотра и редактирования данных,
пароль необходимо шифровать"""

from  SQLstart import*




# Start
print(" Добро пожаловать в систему")

enter = input (" Нажмите 1 для входа в систему или 2 для регистрации ")
while True:
    if enter =="1":
        rezult = input_log()
        print(rezult)
            #if rezult is None:
            #    print(' Пользователь с таким логином не обнаружен, попробуйте заново или зарегистрируйтесь')
            #else:
            #    print(' Добро пожаловать',rezult )

    elif enter =="2":
        input_log()
        while True:
            pas = input_password()
            if pas != None:
                print(shifr(pas))
                break
    else:
        break


'''def registr():
    type = input(" Если Вы преподаватель, нажмите 1, если студент нажмите 2 ")
    name = input(" Введите имя ")
    theme = ''
    lastname = input (" Введите фамилию ")
    faculty  = input (" Введите факультет ")
    if type == "1":
        theme = input ("Введите предмет " )
    elif type == "2":
        theme = input(" Введите номер группы")

    login = input (' Введите логин (не менее 6 символов)')
    password = input (" Введите пароль (не менее 6 символов)")
    return type, name, lastname, faculty, theme, login, password

print(registr())'''

