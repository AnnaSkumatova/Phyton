def Show_Menu():
    print('0. Показать все контакты')
    print('1. Открыть файл с контактами')
    print('2. Записать файл с контактами')
    print('3. Добавить контакт')
    print('4. Изменить контакт')
    print('5. Удалить контакт')
    print('6. Поиск по контактам')

    choice = int(input(' Выберите пункт меню: '))
    return choice

def show_phone_book(phone_book):
    if len(phone_book) < 1:
        print ('Телефонная книга пуста')
    else:
        for item in phone_book:
            print (*item)


def input_path():
    path = input('Введите имя файла: ')
    return path


def input_contact():
    name_contact = input('Введите ФИО контакта: ')
    
    