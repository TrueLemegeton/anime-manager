def main():
    show_menu()

    while True:
        command = input('Выберите нужный пункт: ')

        if command == '1':
            add_anime()
            show_menu()

        elif command == '2':
            delete_anime()
            print()
            show_menu()

        elif command == '3':
            show_anime()
            print()
            show_menu()
            
        elif command == '4':
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

def delete_anime():
    anime_to_delete = input('Введите название аниме, которое хотите удалить: ')

    with open ('anime_list.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()


    with open('anime_list.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            if anime_to_delete.lower() != line.strip().lower():
                file.write(line)

def show_menu():
    print('----------')
    print('Меню: ')
    print('1. Добавить')
    print('2. Удалить')
    print('3. Посмотреть')
    print('4. Выход')
    print('----------')
    print()

if __name__ == '__main__':
    main()