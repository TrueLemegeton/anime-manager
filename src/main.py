def main():

    
    counter = 1
    
    show_menu()

    while True:
        command = input('Выберите нужный пункт: ')

        if command == '1':
            add_anime()
            show_menu()

        if command == '2':
            show_anime()
            print()
            show_menu()
            

        if command == '3':
            print('Выход из программы прошел успешно!')
            break

def add_anime():
    anime_name = input('Введите название аниме: ')
    with open('anime_list.txt', 'a', encoding='utf-8') as file:
        file.write(f'{anime_name}' + '\n')    
    print('Сохранение прошло успешно!')

def show_anime():
    with open('anime_list.txt', 'r', encoding='utf-8') as file:
        print('Мой список аниме!')
        for line in file:
            if line:
                print(line.strip())


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