import json

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
            search_anime()
            print()
            show_menu()

        elif command == '4':
            edit_anime()
            print()
            show_menu()

        elif command == '5':
            show_anime()
            print()
            show_menu()
            
        elif command == '6':
            print('Выход из программы прошел успешно!')
            break

def add_anime():

    anime = {}
    anime['title'] = input('Введите название аниме: ')
    anime['personal_rating'] = float(input('Как вы оцениваете это аниме: '))
    anime['status'] = input('Статус: ')
    anime['review'] = input('Комментарий: ')


    with open('anime.json', mode='r', encoding='utf-8') as file:
        anime_list = json.load(file)

    anime_list.append(anime)

    with open('anime.json', mode='w', encoding='utf-8') as file:
        json.dump(anime_list, file, ensure_ascii=False, indent=2)

    print('Добавление произошло успешно!')


def show_anime():
    with open('anime.json', mode='r', encoding='utf-8') as file:
        inf = json.load(file)

    print('-----------')
    for anime in inf:
        print(f'Название: {anime['title']}')
        print(f'Личная оценка: {anime['personal_rating']}')
        print(f'Статус: {anime['status']}')
        print(f'Комментарий: {anime['review']}')
        print('-----------')

    

def delete_anime():
    anime_to_delete = input('Введите название аниме, которое хотите удалить: ')

    with open ('anime.json', 'r', encoding='utf-8') as file:
        anime_list = json.load(file)

    anime_list = [anime for anime in anime_list if anime['title'].lower() != anime_to_delete.lower()]

    with open ('anime.json', 'w', encoding='utf-8') as file:
        json.dump(anime_list, file, ensure_ascii=False, indent=2)

    print('Удаление произошло успешно!')


def edit_anime():

    anime_to_edit = input('Какое аниме желаете изменить: ')

    with open('anime.json', mode='r', encoding='utf-8') as file:
        anime_list = json.load(file)

    for anime in anime_list:
        if anime['title'].lower() == anime_to_edit.lower():
            print('1. Название')
            print('2. Оценку')
            print('3. Статус')
            print('4. Комментарий')
            choice = input('Что изменить: ')


            if choice == '1':
                new_title = input('Новое название: ')
                anime['title'] = new_title
            if choice == '2':
                new_rating = float(input('Новая оценка: '))
                anime['personal_rating'] = new_rating
            if choice == '3':
                new_status = input('Новый статус: ')
                anime['status'] = new_status
            if choice == '4':
                new_review = input('Новый комментарий: ')
                anime['review'] = new_review
    

    with open('anime.json', mode='w', encoding='utf-8') as file:
        json.dump(anime_list, file, ensure_ascii=False, indent=2)

def search_anime():
    search_title = input('Введите название аниме, которое хотите найти: ')

    with open('anime.json', mode='r', encoding='utf-8') as file:
        anime_list = json.load(file)

    flag = False

    for anime in anime_list:
        if anime['title'].lower() == search_title.lower():
            flag = True
            print('-----------')
            print(f'Название: {anime["title"]}')
            print(f'Личная оценка: {anime["personal_rating"]}')
            print(f'Статус: {anime["status"]}')
            print(f'Комментарий: {anime["review"]}')
            print('-----------')
        break

    if not flag:
        print('Аниме с таким названием не найдено!')


def show_menu():
    print('----------')
    print('Меню: ')
    print('1. Добавить')
    print('2. Удалить')
    print('3. Поиск')
    print('4. Изменить')
    print('5. Посмотреть')
    print('6. Выход')
    print('----------')
    print()

if __name__ == '__main__':
    main()
