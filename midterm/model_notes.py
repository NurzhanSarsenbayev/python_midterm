# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента
#
import json

from datetime import datetime


class ModelNotes:
    # Конструктор, с путём по умолчанию
    def __init__(self, file_path="notes.json"):
        self.file_path = file_path
        self.notes = self.load_notes()
    # Читаем и возвращаем созданный файл, в противном случае возвращаем пустой список
    def load_notes(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    # Открываем наш файл и записываем в него
    def save_notes(self):
        with open(self.file_path, "w") as file:
            json.dump(self.notes, file, indent=2)
    # Определяем дату, определяем id по длине нашего списка, по аргументам определяем Название и Тело заметки
    # Используя save_notes записываем в файл
    def add_note(self, title, body):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        new_note = {"id": len(self.notes) + 1, "title": title, "body": body, "created_at": timestamp}
        self.notes.append(new_note)
        self.save_notes()
    # Находим нужную запись по списку и заменяем поля на наши аргументы. Меняем дату
    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note["id"] == note_id:
                note["title"] = title
                note["body"] = body
                note["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                return True
        return False
    # Удаляем запись
    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note["id"] != note_id]
        self.save_notes()
