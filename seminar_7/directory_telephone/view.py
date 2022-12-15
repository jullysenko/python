def choise():
    print('Привет!\nДоступны дейстия: ')
    print('1. Добавить данные.')
    print('2. Считать данные.')
    cho = input('Сделайте выбор: ')
    return cho

def input_data():
    info = []
    last_name = info.append(input('Напишите фамилию: '))
    first_name = info.append(input('Напишите имя: '))
    telephone = info.append(input('Напишите телефон: '))
    return info
