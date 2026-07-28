def main():

    lst = []
    counter = 1
    
    show_menu()

    while True:
        command = input('Выберите нужный пункт: ')

        if command == '1':
            question = input('Напишите название аниме: ')
            lst.append(f'{counter}. {question}')
            counter += 1
            print()
            show_menu()

        if command == '2':
            print(lst)
            print()
            show_menu()

        if command == '3':
            print('Выход из программы прошел успешно!')
            break


def show_menu():
    print('----------')
    print('Меню: ')
    print('1. Добавить')
    print('2. Посмотреть')
    print('3. Выход')
    print('----------')
    print()

    

if __name__ == '__main__':
    main()