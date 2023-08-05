import json
import os
import datetime

NOTES_FILE = "notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as file:
        return json.load(file)

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().isoformat()

    notes = load_notes()
    note = {"id": len(notes) + 1, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    save_notes(notes)

def view_notes():
    notes = load_notes()
    for note in notes:
        print(f"[{note['id']}] {note['title']} ({note['timestamp']})")
    print()

def view_note():
    note_id = int(input("Введите номер заметки для просмотра: "))
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата создания/изменения: {note['timestamp']}")
            return
    print("Заметка с таким номером не найдена.")

def edit_note():
    note_id = int(input("Введите номер заметки для редактирования: "))
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note["title"] = title
            note["body"] = body
            note["timestamp"] = datetime.datetime.now().isoformat()
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с таким номером не найдена.")

def delete_note():
    note_id = int(input("Введите номер заметки для удаления: "))
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка с таким номером не найдена.")

def main():
    while True:
        print("1. Просмотреть список заметок")
        print("2. Просмотреть заметку по номеру")
        print("3. Добавить новую заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("0. Выйти из программы")
        choice = input("Выберите действие: ")

        if choice == "1":
            view_notes()
        elif choice == "2":
            view_note()
        elif choice == "3":
            add_note()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "0":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
