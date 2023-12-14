from model_notes import ModelNotes
from view_notes import ViewNotes


class ControllerNotes:
    # Конструктор
    def __init__(self):
        self.model = ModelNotes()
        self.view = ViewNotes()
    # Показываем наши записи, метод из View и аргумент Model
    def list_notes(self):
        self.view.display_notes(self.model.notes)
    # Добавляем записи, запрашивая у пользователя ввод и затем добавляя их с помощью add_note из Model
    def add_note(self):
        title = self.view.input_string("Enter note title: ")
        body = self.view.input_string("Enter note body: ")
        self.model.add_note(title, body)
        print("Note added successfully.")
    # Изменяем наши записи. Находим по id.
    def edit_note(self):
        note_id = self.view.input_int("Enter note ID to edit: ")
        note = next((note for note in self.model.notes if note["id"] == note_id), None)
        if note:
            print(f"Note Title: {note['title']}")
            print(f"Note Body: {note['body']}")
        else:
            print("Note not found.")
        title = self.view.input_string("Enter new title: ")
        body = self.view.input_string("Enter new body: ")
        if self.model.edit_note(note_id, title, body):
            print("Note edited successfully.")
        else:
            print("Note not found.")
    # Удаляем запись по id
    def delete_note(self):
        note_id = self.view.input_int("Enter note ID to delete: ")
        self.model.delete_note(note_id)
        print("Note deleted successfully.")
    # Основной метод, связывающий всё остальное. if/elif/break для имитации меню выбора
    def run(self):
        while True:
            print("\nCommands:")
            print("1. List notes")
            print("2. Add note")
            print("3. Edit note")
            print("4. Delete note")
            print("5. Exit")

            choice = self.view.input_string("Enter the number of your choice: ")

            if choice == "1":
                self.list_notes()
            elif choice == "2":
                self.add_note()
            elif choice == "3":
                self.edit_note()
            elif choice == "4":
                self.delete_note()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    controller = ControllerNotes()
    controller.run()
