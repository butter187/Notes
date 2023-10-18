import json
import datetime


def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


notes = load_notes()


def add_note():
    title = input("Заголовок заметки: ")
    text = input("Заметка: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        'id': len(notes) + 1,
        'title': title,
        'text': text,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)


def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)


def delete_note():
    note_id = int(input("Введите id заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена")
            return
    print("Заметка не найдена")


def edit_note():
    note_id = int(input("Введите id заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            new_title = input("Новый заголовок заметки: ")
            new_text = input("Новый текст заметки: ")
            note['title'] = new_title
            note['text'] = new_text
            note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка отредактирована")
            return
    print("Заметка с id не найдена")


def search_notes():
    date_str = input("Введите дату для поиска заметки (YYYY-MM-DD): ")
    try:
        find_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Некорректный формат даты")
        return

    find_notes = [note for note in notes if
                      datetime.datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S").date() == find_date]

    if find_notes:
        print("Заметки на указанную дату:")
        for note in find_notes:
            print(f"id: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело: {note['text']}")
            print(f"Дата/Время создания или последнего изменения: {note['timestamp']}")
            print()
    else:
        print("Заметки на указанную дату не найдены")


def print_notes():
    for note in notes:
        print(f"id: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело: {note['text']}")
        print("\n")


def menu():
    menu_points = ['Открыть',
                   'Добавить заметку',
                   'Сохранить заметку',
                   'Изменить заметку',
                   'Удалить заметку',
                   'Найти заметку',
                   'Напечатать',
                   'Выход']
    print('Главное меню:')
    [print(f'\t{i}. {item}') for i, item in enumerate(menu_points, 1)]
    choise = int(input('Выберите пункт меню: '))
    return choise


while True:
    choice = menu()
    match choice:
        case 1:
            load_notes()
        case 2:
            add_note()
            print("Заметка добавлена")
        case 3:
            save_notes(notes)
            print('Заметка сохранена')
        case 4:
            edit_note()
            print("Заметка изменена")
        case 5:
            delete_note()
            print("Заметка удалена")
        case 6:
            search_notes()
        case 7:
            print_notes()
        case 8:
            print('\nНу всё, пока!')
            break
