#Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона, адрес - данные, которые должны находиться в файле.
###Программа должна выводить данные
#Программа должна сохранять данные в текстовом файле
#Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
#Использование функций. Ваша программа не должна быть линейной

# 1. Создать файл phonebook.txt
#   - обратимся к файлу phonebook.txt в режиме append ('a')

# 2. Ввод данных
#   - получить от пользователя данные по новому контатку
#   - подготовить данные к записи
#   - обратимся к файлу phonebook.txt в режиме append ('a')
#   - добавить полученные данные

# 3. Вывод всех данных на экран
#   - обратимся к файлу phonebook.txt в режиме read ('r')
#   - вывести на экран данные

# 4. Пользовательский поиск по характеристике
#   - Выбрать вариант поиска (по имени, фамилии или телефону)
#   - Получить данные для поиска 
#   - обратимся к файлу phonebook.txt в режиме read ('a')
##  - осуществим поиск по файлу
#   - выведем на экран найденные совпадения

# 5. Пользовательский интерфейс
#
#

#('phonebook.txt','a')

def file_read():
    with open('phonebook.txt','r', encoding='UTF-8') as file:
        return file.read()

def file_append(text=''):
    with open('phonebook.txt','a', encoding='UTF-8') as file:
        file.write(text)

def input_name():
    return input('Введите имя ')

def input_son():
    return input('Введите фамилию ')

def input_pat():
    return input('Введите отчество ')

def input_ph():
    return input('Введите телефон ')

def input_adr():
    return input('Введите адрес ')

def input_data():
    son = input_son()
    name = input_name()
    pat = input_pat()
    ph = input_ph()
    adr = input_adr()

    contact_str = f"{son} {name} {pat} {ph}\n{adr}\n\n"
    file_append(contact_str)

def print_data():
    print(file_read())

def searsh_contact_one_version():
    search = input("Введите данные для поиска: ")
    contacts_list = file_read().split("\n\n") #разбиваем весь текст в файле на строки 
    #print([contacts_list])
    for contact_str in contacts_list:  #ищем совпадение 
        if search in contact_str:
            print(contact_str)

def searsh_contact_two_version():
    print('Возможные варианты поиска: \n'
         "1. По фамилии\n"
         "1. По имени\n"
         "1. По отчеству\n"
         "1. По номеру телефона\n"
         "1. По адресу\n")
    command = input("Выберите вариант поиска: ")

    while command not in ('1','2','3','4','5'):
        print('Некорректный ввод')
        command = input("Выберите вариант поиска: ")

    i_search = int(command)-1

    search = input("Введите данные для поиска: ")
    contacts_list = file_read().rstrip().split("\n\n") #разбиваем весь текст в файле на строки. Rstrip для удаления пробелов
    #print([contacts_list])
    for contact_str in contacts_list:  #ищем совпадение 
        cont_list = contact_str.replace('\n',' ').split()
        if search in cont_list[i_search]:
            print(contact_str)

searsh_contact_two_version()
#file_append()
#input_data()
#print_data()
