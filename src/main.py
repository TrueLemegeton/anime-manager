from ui import show_menu
from utils import pause_and_clear_console
from operations import (
    show_anime,
    search_anime,
    add_anime, 
    delete_anime, 
    edit_anime, 
    sort_anime, 
    filter_anime
)


def main() -> None:
    """Run the application and process user commands."""
    show_menu()

    while True:
        command = input('Выберите нужный пункт: ').strip()

        if command == '1':
            add_anime()

        elif command == '2':
            delete_anime()

        elif command == '3':
            search_anime()

        elif command == '4':
            sort_anime()

        elif command == '5':
            filter_anime()

        elif command == '6':
            edit_anime()

        elif command == '7':
            show_anime()
            
        elif command == '8':
            print('Выход из программы прошел успешно.')
            break

        else:
            print('Некорректная команда. Попробуйте снова.')
            pause_and_clear_console()
            show_menu()
            continue

        pause_and_clear_console()
        show_menu()

if __name__ == '__main__':
    main()
