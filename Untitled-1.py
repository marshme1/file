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
import os 

def file_read(file_d = 'phonebook.txt'):
    
    with open(file_d,'r', encoding='UTF-8') as file:
        return file.read()

def file_append(text='', file_d = 'phonebook.txt'):
    with open(file_d,'a', encoding='UTF-8') as file:
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

def input_data(file_d = 'phonebook.txt'):
    global id
    contacts_list = file_read().rstrip().split("\n\n") #разбиваем весь текст в файле на строки. Rstrip для удаления пробелов
    if file_read(file_d)=='':
        id =1
    else:
        id=len(contacts_list)+1
    son = input_son()
    name = input_name()
    pat = input_pat()
    ph = input_ph()
    adr = input_adr()

    contact_str = f"{id} {son} {name} {pat} {ph}\n{adr}\n\n"
    #id = id+1
    file_append(contact_str, file_d)



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
         "2. По имени\n"
         "3. По отчеству\n"
         "4. По номеру телефона\n"
         "5. По адресу\n")
    command = input("Выберите вариант поиска: ")

    while command not in ('1','2','3','4','5'):
        print('Некорректный ввод')
        command = input("Выберите вариант поиска: ")

    i_search = int(command)

    search = input("Введите данные для поиска: ")
    contacts_list = file_read().rstrip().split("\n\n") #разбиваем весь текст в файле на строки. Rstrip для удаления пробелов
    #print([contacts_list])
    for contact_str in contacts_list:  #ищем совпадение 
        cont_list = contact_str.replace('\n',' ').split()
        if search in cont_list[i_search]:
            print(contact_str)

def copy_data(file_d, list):
        
    isFile=os.path.isfile(f"G:\Python\{file_d}") 
    if not isFile:
        file_append('', file_d)
    contacts_list = file_read(file_d).rstrip().split("\n\n") #разбиваем весь текст в файле на строки. Rstrip для удаления пробелов
    
    if file_read(file_d)=='':
        id =1
    else:
        id=len(contacts_list)+1
    son = list[1]
    name = list[2]
    pat = list[3]
    ph = list[4]
    adr = list[5]

    contact_str = f"{id} {son} {name} {pat} {ph}\n{adr}\n\n"
    #id = id+1
    file_append(contact_str, file_d)

def copy_contact():
    #with open('phonebook.txt','r') as firstfile, open('second.txt','a') as secondfile:
        #for line in firstfile: 
            #secondfile.write(line)
    number = input("Введите номер строки для копирования: ")


    contacts_list = file_read().rstrip().split("\n\n")
    
    flag = False
    file = input("Введите название файла, куда требуется скопировать контакт: ")
    contacts_list = file_read().rstrip().split("\n\n") #разбиваем весь текст в файле на строки. Rstrip для удаления пробелов
    for contact_str in contacts_list:  #ищем совпадение 
        cont_list = contact_str.replace('\n',' ').split()
        if number in cont_list[0]:
            copy_data(file, cont_list)
            flag = True
           
    if flag == False:
        print('Такой строки нет!')   
            
        

def u_interface():
    command = ""
    while command !="5":
        print('Меню: \n'
            "1. Добавить контакт\n"
            "2. Найти контакт\n"
            "3. Вывести все контакты\n"
            "4. Копировать контакт в другой файл\n"
            "5. Выход\n")
        command = input("Выберите пункт меню: ")
        while command not in ('1','2','3','4','5'):
            print('Некорректный ввод')
            command = input("Выберите пункт меню: ")

        match command:
            case "1":
                input_data()
            case "2":
                searsh_contact_two_version()
            case "3":
                print_data()
            case "4":
                copy_contact()
            case "5":
                print("Всего хорошего")
u_interface()
#searsh_contact_two_version()
#file_append()
#input_data()
#print_data()
#copy_contact()

#contact_str = f"{id} {son} {name} {pat} {ph}\n{adr}\n\n"