
def show_all(file_name:str):
    with open(file_name, 'r',encoding='utf-8') as f:
         data = f.readlines()
         print("".join(data))

def add_new(file_name: str):
    #data = input('Введите ФИО и номер телефона через пробел')
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_num = input('Введите номер телефона: ')
    #f = open(file_name, 'a' , encoding='utf=8')
    #f.close()
    with open(file_name, 'a' , encoding='utf=8') as fd:
        fd.write(f'{last_name }, {first_name}, {patronymic}, {phone_num}\n')

def remove(file_name: str):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_num = input('Введите номер телефона: ')
    data = ''
    with open(file_name, 'r' , encoding='utf=8') as f:
        data = f.readlines()
        s = f'{last_name }, {first_name}, {patronymic}, {phone_num}\n'
        data.remove(s)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(data)  

def mod(file_name:str):
    old_data = search(file_name, True)
    print("Введите новые данные:\n")
    last_name_ = input('Введите фамилию: ')
    first_name_ = input('Введите имя: ')
    patronymic_ = input('Введите отчество: ')
    phone_number_ = input('Введите номер телефона: ')
    data = ""
    with open(file_name, 'r',encoding='utf-8') as f:
          data = f.readlines()
    i = data.index(old_data)
    data[i] = f'{last_name_}, {first_name_}, {patronymic_}, {phone_number_}\n'

    with open(file_name, 'w',encoding='utf-8') as f:\
          f.writelines(data)
def search(file_name:str,option: bool):
     c = input("Введите:\n 1 - для поиска по фамилии: \n 2 - для поиска по имени: ")
     opt = 0
     if c == '1':
        opt = 0
     elif c == '2':
          opt = 1


def main():
    file_name = 'phonebook.txt'
    flag_exit = False
    while not flag_exit:
        print('1 - показать все записи')
        print('2 - добавить все записи')
        print('3 - удалить запись')
        print('4 - изменить запись')
        print('5 - поиск записи')
        answer = input('Введите операцию или x для выхода: ')
        if answer == '1':
            show_all(file_name=file_name)
        elif answer == '2':
            add_new(file_name) 
        elif answer == '3':
            remove(file_name)
        elif answer == '4':
            mod(file_name)
        elif answer == '5':
         print(search(file_name,False))
        elif answer == 'x':
            flag_exit = True    

if __name__ == '__main__':
 main()            
