
def show_all():
    pass 

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

def main():
    file_name = 'phonebook.txt'
    flag_exit = False
    while not flag_exit:
        print('1 - показать все записи')
        print('2 - добавить все записи')
        answer = input('Введите операцию или x для выхода: ')
        if answer == '1':
            show_all()
        elif answer == '2':
            add_new(file_name)    
        elif answer == 'x':
            flag_exit = True    

if __name__ == '__main__':
     main()