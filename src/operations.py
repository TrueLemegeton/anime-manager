from storage import load_anime, save_anime
from ui import show_info


def show_anime() -> None:
    """Display the list of anime."""
    anime_list = load_anime()

    if not anime_list:
        print('Список анмие пуст!')
        return
    
    for anime in anime_list:
        show_info(anime)


def search_anime() -> None:
    """Search for an anime by title."""
    search_title = input('Введите название аниме, которое хотите найти: ').strip().lower()
    

    anime_list = load_anime()

    for anime in anime_list:
        if anime['title'].lower() == search_title:
            show_info(anime)
            return
            
    print('Аниме с таким названием не найдено!')


def add_anime() -> None:
    """Add a new anime to the list."""

    anime = {}
    anime['title'] = input('Введите название аниме: ').strip()

    print('1. Просмотрено')
    print('2. Смотрю')
    print('3. Планирую смотреть')
    print('4. Брошено')
    status_option = input('Выберите статус: ')

    if status_option == '1':
        anime['status'] = 'Просмотрено'
        rating = input('Как вы оцениваете это аниме (необязательно): ').strip()

        if rating and not rating.replace('.', '', 1).isdigit():
            print('Некорректная оценка. Оценка будет установлена как None.')
            rating = None

        anime['personal_rating'] = float(rating) if rating else None

        review = input('Ваш комментарий (необязательно): ').strip()
        anime['review'] = review if review else None

    elif status_option == '2':
        anime['status'] = 'Смотрю'
        anime['personal_rating'] = None
        anime['review'] = None

    elif status_option == '3':
        anime['status'] = 'В планах'
        anime['personal_rating'] = None
        anime['review'] = None

    elif status_option == '4':
        anime['status'] = 'Брошено'
        anime['reason'] = input('Причина (необязательно):')
        anime['personal_rating'] = None
        anime['review'] = None

    else:
        print('Некорректный выбор статуса. Аниме не будет добавлено.')
        return

    anime_list = load_anime()
    anime_list.append(anime)
    save_anime(anime_list)

    print('Добавление произошло успешно!')


def delete_anime() -> None:
    """Delete an anime from the list."""
    anime_to_delete = input('Введите название аниме, которое хотите удалить: ').strip().lower()

    anime_list = load_anime()
    old_length = len(anime_list)

    
    anime_list = [anime for anime in anime_list if anime['title'].lower() != anime_to_delete]

    if len(anime_list) < old_length:
        save_anime(anime_list)
        print('Удаление произошло успешно!')
    else:
        print('Аниме с таким названием не найдено. Удаление не произошло.')
    

def edit_anime() -> None:
    """Edit an existing anime in the list."""

    anime_to_edit = input('Какое аниме желаете изменить: ').strip()

    anime_list = load_anime()

    for anime in anime_list:
        if anime['title'].lower() == anime_to_edit.lower():
            print('1. Название')
            print('2. Оценку')
            print('3. Статус')
            print('4. Комментарий')
            print('5. Причина (если брошено)')
            choice = input('Что изменить: ').strip()

            if choice == '1':
                new_title = input('Новое название: ').strip()
                anime['title'] = new_title

            elif choice == '2':
                new_rating = input('Новая оценка: ').strip()

                if not new_rating.replace('.', '', 1).isdigit():
                    print('Некорректная оценка. Изменение не будет выполнено.')
                    return

                new_rating = float(new_rating)
                
                if not 0 <= new_rating <= 10:
                    print('Оценка должна быть от 0 до 10.')
                    return

                anime['personal_rating'] = new_rating

            elif choice == '3':
                print('1. Просмотрено')
                print('2. Смотрю')
                print('3. Планирую смотреть')
                print('4. Брошено')
                new_status = input('Выберите статус: ').strip()

                if new_status == '1':
                    anime['status'] = 'Просмотрено'
                elif new_status == '2':
                    anime['status'] = 'Смотрю'
                elif new_status == '3':
                    anime['status'] = 'В планах'
                elif new_status == '4':
                    anime['status'] = 'Брошено'
                else:
                    print('Некорректный выбор статуса.')
                    return

            elif choice == '4':
                new_review = input('Новый комментарий: ').strip()
                anime['review'] = new_review

            elif choice == '5':
                new_reason = input('Новая причина: ').strip()
                anime['reason'] = new_reason

            else:
                print('Некорректный выбор. Изменение не будет выполнено.')
                return


            save_anime(anime_list)
            print('Изменение произошло успешно.')
            return

    print('Аниме с таким названием не найдено!')


def sort_anime() -> None:
    """Sort the list of anime by a chosen criterion."""
    anime_list = load_anime()

    print('1. Название')
    print('2. Личная оценка')
    print('3. Статус')
    choice = input('По какому критерию сортировать: ').strip()

    if choice == '1':
        sorted_list = sorted(anime_list, key=lambda x: x['title'])

    elif choice == '2':
        sorted_list = sorted(
            anime_list, 
            key=lambda x: x['personal_rating'] if x['personal_rating'] is not None else -1, 
            reverse=True)
        
    elif choice == '3':
        sorted_list = sorted(anime_list, key=lambda x: x['status'])
          
    else:
        print('Некорректный выбор критерия сортировки.')
        return

    for anime in sorted_list:
        show_info(anime)

    print('Сортировка прошла успешно.')


def filter_anime() -> None:
    """Filter the list of anime by a chosen criterion."""
    anime_list = load_anime()

    if not anime_list:
        print('Список аниме пуст.')
        return

    print('1. Оценка')
    print('2. Статус')
    choice = input('По какому критерию фильтровать: ').strip()

    if choice == '1':
        rating = input('Введите минимальную оценку: ').strip()

        if not rating.replace('.', '', 1).isdigit():
            print('Некорректная оценка. Фильтрация не будет выполнена.')
            return

        rating_threshold = float(rating)

        if not 0 <= rating_threshold <= 10:
            print('Оценка должна быть от 0 до 10.')
            return

        filtered_list = [
            anime
            for anime in anime_list
            if anime.get('personal_rating') is not None
            and anime['personal_rating'] >= rating_threshold
        ]

    elif choice == '2':
        print('Доступные статусы:')
        print('- Просмотрено')
        print('- Смотрю')
        print('- В планах')
        print('- Брошено')

        status_filter = input('Введите статус: ').strip()

        filtered_list = [
        anime
        for anime in anime_list
        if anime['status'].lower() == status_filter.lower()
    ]

    else:
        print('Некорректный выбор критерия.')
        return

    if not filtered_list:
        print('Подходящих аниме не найдено.')
        return

    for anime in filtered_list:
        show_info(anime)

    print('Фильтрация прошла успешно!')