# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# r - только чтение файла
# a - дозаписать в файл
# w - перезапись файла



def show_data(FNAME):
    '''Функция показывает содержимое справочника'''
    try:
        with open(FNAME, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print("Файл отсутствует")

def new_data(FNAME):
    '''Функция добавляет новую информацию'''
    with open(FNAME, 'a', encoding='utf-8') as file:
        file.write(input('Введите данные:') + '\n')

def find_data(FNAME):
    '''Функция ищет информацию в справочнике'''
    with open(FNAME, 'r', encoding='utf-8') as file:
        search = input("Введите информацию для поиска ")
        temp = file.read().split('\n')
        result=[(temp.index(i), i)
                    for i in temp 
                    if search.lower() in i.lower()]
        if len(result)>=1:
            [print(f'{result.index(i)+1}) {str(i[1])}') for i in result]
            return([line[0]for line in result], temp)
        else:
            print('Ничего не найдено')
            return([], temp)
    
def rename(strings, data, FNAME):
    fio = input("Введите новое ФИО: ")
    phone = input("Введите новый телефон: ")
    with open(FNAME, 'w', encoding='utf-8')as f2:
        [f2.write(f'{fio} | {phone}\n') if line == strings else f2.write(
            f'{data[line]}\n') for line in range(len(data)-1)]
        print('данные изменены')
def delete(strings,data,FNAME):
    with open(FNAME, 'w', encoding='utf-8')as f2:
        [f2.write(f'\n') if line == strings else f2.write(
            f'{data[line]}\n') for line in range(len(data)-1)]
        print('данные удалены')
def editor_data(FNAME):
    data=find_data(FNAME)
    if len(data[0]) == 1:
        rename(data[0][0], data[1], FNAME)
    elif len(data[0]) > 1:
        change = int(input("Введите порядковый номер изменяемой строки"))
        while change not in [i for i in range(1, len(data[0])+1)]:
            print("введенного номера нет в списке")
            change = int(input('Введите порядковый номер изменяемой строки'))
        rename(int(data[0][change-1]), data[1], FNAME)

def delete_data(FNAME): 
    data=find_data(FNAME)
    if len(data[0]) == 1:
        delete(data[0][0], data[1], FNAME)
    elif len(data[0]) > 1:
        change = int(input("Введите порядковый номер изменяемой строки"))
        while change not in [i for i in range(1, len(data[0])+1)]:
            print("введенного номера нет в списке")
            change = int(input('Введите порядковый номер удаляемой строки'))
        delete(int(data[0][change-1]), data[1], FNAME)
def menu():        
    import os
    FNAME='13.txt'
    while True:
        os.system('cls')
        mode = input("Выберите режим работы справочника:\
                    \n 1. Функция показывает содержимое справочника:\
                    \n 2. Функция добавляет новую информацию\
                    \n 3. Функция ищет информацию в справочнике\
                    \n 4. Функция ищет информацию и редактирует\
                    \n 5. Функция удаляет контакт\
                     \n 0. Завершение работы справочника: ")
        if mode == '1':
            print(show_data(FNAME))
        elif mode == '2':
            new_data(FNAME)
        elif mode == '3':
            find_data(FNAME)
        elif mode == '4':
            editor_data(FNAME)
        elif mode == '5':
            delete_data(FNAME)    
        elif mode == '0':
            break
        else:
            print('no mode')
menu()
