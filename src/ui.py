def show_info(anime: dict) -> None:
    """Display information about an anime."""
    print('-----------')
    print(f'Название: {anime["title"]}')
    print(f'Личная оценка: {anime.get("personal_rating", "Не указана")}')
    print(f'Статус: {anime["status"]}')
    print(f'Комментарий: {anime.get("review", "Не указан")}')
    print('-----------')


def show_menu() -> None:
    """Display the main menu."""
    print('----------')
    print('Меню: ')
    print('1. Добавить')
    print('2. Удалить')
    print('3. Поиск')
    print('4. Сортировка')
    print('5. Фильтрация')
    print('6. Изменить')
    print('7. Посмотреть')
    print('8. Выход')
    print('----------')
    print()