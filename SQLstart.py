""" Создать базу данных для преподавателей и студентов, с возможностью добавления, просмотра и редактирования данных,
пароль необходимо шифровать"""

from  SQLdatabase import*

def start():                                        # функция старта программы
    print("Добро пожаловать в систему")
    while True:
        enter = input ("Нажмите 1 для входа в систему или 2 для регистрации ")
        if enter =="1":                             # возвращает ID пользователя
            ide = start_entrance()
            if ide is not None:
                return ide, None
        elif enter =="2":                           # возвращает новые логин и пароль
            lpas = start_register()
            if lpas is not None:
                return lpas
        else:
            break



def start_entrance():                           # функция ввода и проверки логина для входа в систему
    log = input("Введите логин ")
    rezult = input_log(log)
    if rezult is None:
        print('Пользователь с таким логином не обнаружен, попробуйте заново или зарегистрируйтесь')
    else:
        new_password = shifr_password()         # проверка на соответствие пароля
        if new_password == rezult[2]:
            print('И снова здравствуйте', )
            return rezult[0]
        else:
            print("Неверный пароль")

def start_register():                           # функция регистрации нового пользователя (логин, пароль)
    log= input("Введите логин ")
    rezult = input_log(log)
    if rezult is not None:
        print ('Пользователь с таким логином уже зарегистрирован')

    else:
        pas1 = shifr_password()
        print('Повторите ввод пароля...')
        pas2 = shifr_password()
        if pas1 != pas2:
            print('Пароли не совпадают, повторите попытку')
            return None
        return log, pas2



def registr(login, password):                           # функция добавления данных нового пользователя
    name = input("Введите имя ")                        # возвращает введенные данные
    lastname = input ("Введите фамилию ")
    faculty = input("Введите факультет ")
    type = input("Если Вы преподаватель, нажмите 1, если студент нажмите 2 ")
    if type == "1":
        theme = input ("Введите предмет " )
    elif type == "2":
        theme = input("Введите номер группы ")

    return login, password,  name, lastname, faculty, type, theme

data = start()                              # старт программы

if data is None:                            # выход из программы если не выбраны нужные параметры(1 или2)
    print('Всего наилучшего!')
elif data[1] is None:                       # ecли возвращается только ID то переходим к чтению базы
    person=DataBase()
    data =person.getFullUser(data[0])
    print(data[0]['lastname'],data[0]['name'])                  # печатаем имя и фамилию пользователя
    if data[0]['type'] == 1:                                    # если тип 1-преподаватель, то :
        while True:
            enter = input("Выберите действия: 1-добавить пользователя, 2 - просмотреть информацию, 3 - поставить оценку, 4- изменить оценку, 5 -выход ")
            if enter == "1":
                data = start_register()
                if data == None:
                    data = start()
                else:
                    nextdata = registr(data[0], data[1])

                    print('Имя:', nextdata[2], 'Фамилия:', nextdata[3], 'Факультет:', nextdata[4], 'Предмет/Группа', nextdata[6])
                    enter = input('Записать данные?  1 -ДА, 0 -НЕТ ')
                    if enter == '1':
                        record_lpas(data[0], data[1])
                        dataid = read_id(data[0])
                        record_fullus(dataid, nextdata[2], nextdata[3], nextdata[4], nextdata[5], nextdata[6])
                        print('Пользователь успешно зарегистрирован')
            elif enter =='2':
                numbergroup = input('Введите номер группы: ')
                qwer = DataBase()
                users =qwer.getFullUserall()
                counttheme = 0
                for i in range(len(users)):
                    if users [i]['type'] == 2 and numbergroup==users [i]['theme']:
                        print('студент:', users[i]['name'], users[i]['lastname'], '  факультет:', users[i]['faculty'], '  группа:', users[i]['theme'])
                        counttheme +=1
                if counttheme == 0:
                    print('Такой группы нет, выберете другую группу')


            elif enter == '3':
                itemname = input('Введите предмет ')
                groupnumber = input ('Введите номер группы ')
                qwer = DataBase()
                users = qwer.getFullUserall()
                for i in range(len(users)):
                    if users[i]['theme'] == groupnumber:
                        print(users[i]['name'], users[i]['lastname'], users[i]['faculty'], users[i]['theme'])
                        note = input ('Введите оценку ')
                        item = qwer.addMatter(users[i]['ID'],users[i]['theme'], itemname, note)
                del qwer
            elif enter == '4':
                qwer = DataBase()
                matter = qwer.getMatter()
                fullusers = qwer.getFullUserall()
                lastname = input ('Введите фамилию студента: ')
                countname = 0
                for i in  range(len(fullusers)):
                    if fullusers[i]['lastname'] == lastname:
                        countname +=1
                        id =fullusers[i]['ID']
                        for e in range(len(matter)):
                            if matter[e]['ID']== id:
                                print ("Студент: ", fullusers[i]['name'], fullusers[i]['lastname'], ' Предмет:',matter[e]['theme'], " Оценка:", matter[e]['note'])
                                a= input ("Если хотите изменить оценку нажмите 1  ")
                                if a =="1":
                                    newnote = input ('Введите новую оценку ')
                                    upd = qwer.updateMatter(id, matter[e]['theme'], newnote)
                                    print("Оценка изменена, новая оценка", newnote)
                if countname ==0:
                    print ('Студента с такой фамилией в списках нет ')


            else:
                print('До новых встреч', data[0]['name'])
                break
    else:
        qwer = DataBase()
        note = qwer.getMatter()

        while True:
            enter = input("Для просмотра оценок и среднего балла нажмите 1,  для выхода из системы 2 ")
            if enter =="1":
                print('Ваши предметы и оценки:')
                rating = 0                              # счетчик оценок
                count = 0
                for i in range(len(note)):              # цикл по ID студента
                    if note[i]['ID'] == data[0]['ID']:
                        print(note[i]['theme'], note[i]['note'])
                        rating += note[i]['note']
                        count +=1
                if count == 0:
                    print('У Вас еще не выставлены оценки ')
                else:
                    print('Ваш средний бал', round((rating/count),2))
            else:
                print('До новых встреч',data[0]['name'])
                break

else:
    data = registr(data[0], data[1])        # если возвращается Логин и пароль переходим к записи нового пользователя
    print("Ваши данные")
    print ( 'Имя:',data[2], '   Фамилия:',data[3],'   Факультет:',data[4],'   Предмет/Группа: ',data[6])
    enter = input('Записать данные?  1 -ДА, 0 -НЕТ ')
    if enter =='1':
        record_lpas(data[0], data[1])
        dataid = read_id(data[0])
        record_fullus(dataid, data[2], data[3], data[4], data[5], data[6])
        print('Вы успешно зарегистрированы, перезайдите в систему')
    elif enter =='0':
        print('Попробуйте еще раз', data[2])




