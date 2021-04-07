""" Создать базу данных для преподавателей и студентов, с возможностью добавления, просмотра и редактирования данных,
пароль необходимо шифровать"""

from  SQLstart import*




def start():
    print(" Добро пожаловать в систему")
    while True:
        enter = input ("Нажмите 1 для входа в систему или 2 для регистрации ")
        if enter =="1":
            rezult = input_log()
            if rezult is None:
                print('Пользователь с таким логином не обнаружен, попробуйте заново или зарегистрируйтесь')
            else:
                new_password =shifr_password()
                if new_password == rezult[2]:
                    print('Добро пожаловать', )
                    return rezult[0]
                else:
                    print("Неверный пароль")


        elif enter =="2":
            rezult = input_log()
            if rezult is not None:
                print('Пользователь с таким логином уже зарегистрирован')
            else:
                print(shifr_password())
                print('Повторите ввод пароля...' )

                break
        else:
            break

print(start())


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

