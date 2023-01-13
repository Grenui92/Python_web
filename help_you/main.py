import os
from os import getlogin
from sys import platform

from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter

from contact_classes.contact_work import WorkContact
from file_sorter import sort_targets
from instructions import show_instructions
from note_classes.note_work import WorkNote
from bug_catcher import erorr_catcher


class UserInterface:

    def __init__(self):
        self.absolute_path = self.create_path_for_saves()
        self.book = WorkContact(f"{self.absolute_path}/contacts.bin")
        self.notes = WorkNote(f"{self.absolute_path}/notes.bin")
        self.commands = {"help": self.help_me,
                         "instruction": self.instructions,

                         "create_contact": self.book.create,
                         "show_contact_book": self.book.show_all,
                         "show_contact": self.book.show_one,
                         "show_contact_page": self.book.show_page,
                         "clear_contact_book": self.book.delete_all,
                         "delete_contact": self.book.delete_one,
                         "add_to_contact": self.book.add_value,
                         "edit_contact": self.book.edit_information,
                         "edit_contact_name": self.book.edit_name,
                         "search_in_contacts": self.book.search_in,

                         "show_nearest_birthdays": self.book.show_nearest_birthdays,
                         "days_to_birthday_for_one": self.book.days_to_birthday_for_one,
                         "days_to_birthday_for_all": self.book.days_to_birthday_for_all,

                         "create_note": self.notes.create,
                         "show_note_book": self.notes.show_all,
                         "show_note": self.notes.show_one,
                         "show_note_page": self.notes.show_page,
                         "clear_note_book": self.notes.delete_all,
                         "delete_note": self.notes.delete_one,
                         "add_to_note": self.notes.add_value,
                         "edit_note": self.notes.edit_information,
                         "edit_note_name": self.notes.edit_name,
                         "search_in_notes": self.notes.search_in,
                         "sorted_notes_by_tags": self.notes.sorted_by_tags,

                         "file_sorter": self.file_sorter,

                         "exit": self.good_bye}


    def run(self):
        """Основна функція. Приймаємо текст, парсимо його, передаємо в хендлер. Виводимо результат."""
        while True:
            print("\nCommand 'help' will help you.")
            data = self.__input_user_text()
            try:
                command, name, data = self.__parse_user_text(data)
            except ValueError:
                print("Enter some information please")
                continue
            result = self.__handler(command, name, data)
            self.__show_results(result)

    @erorr_catcher
    def __input_user_text(self) -> str:
        """Просто зчитує текст."""
        commands_completer = self.commands
        users = {k: None for k in self.book.contacts_book}
        input_completer = NestedCompleter.from_nested_dict({k: users for k in commands_completer})
        data = prompt("Please enter what do you want to do: ", completer=input_completer)
        return data

    @staticmethod
    @erorr_catcher
    def __parse_user_text(text: str) -> list:
        """Обробка тексту. Поділяє текст на три частини, у разі виклику юзером команди яка не потребує аргументів - повертає все одно список
        з трьох елементів, щоб виклик всіх команд був однаковий."""

        data = text.split()
        if len(data) == 1:
            return [data[0], "", ""]
        else:
            return [data[0], data[1], data[2:]]

    @erorr_catcher
    def __handler(self, command: str, name: str, data) -> str | list:
        """Перевірка команди на наявність в нашому словнику і відповідно виклик функції, якщо команда існує, або рейз помилки. Ця помилка обрана,
        щоб відокремитися від KeyError. Коли декоратор ловить цей Warning - він має запускати процес аналізу і підказки команд."""

        if command in self.commands:
            return self.commands[command](name, data)
        else:
            raise Warning(command, self.commands.keys())

    @staticmethod
    def help_me(*_) -> str:
        return "If you want to know how to use this script - use command 'instruction' with:\n" \
               "'contacts' - to read about ContactBook commands.\n" \
               "'notes' - to read about NoteBook commands.\n" \
               "'file_sorter' - to read about FileSorter.\n" \
               "Or use 'exit' if you want to leave."

    @staticmethod
    @erorr_catcher
    def instructions(category: str, *_) -> str:
        """Обирає який файл інструкцій відкрити відповідно до команди користувача."""

        result = show_instructions(category)
        return result

    @erorr_catcher
    def __show_results(self, result: str | list):
        """Виводить результат запросу користувача. Вдалий чи не вдалий - все одно виводить. Навіть декоратор якщо ловить помилку - він не принтує
        рядок, а ретюрнить його сюди. Всі принти мають виконуватися саме тут. І ніде більше в програмі. Окрім FileSorter"""

        if isinstance(result, list):
            for page in result:
                print(page)
        else:
            print(result)

    @erorr_catcher
    def good_bye(self, *_):
        print(self.book.save_to_file())
        print(self.notes.save_to_file())
        exit("Bye")

    @staticmethod
    @erorr_catcher
    def file_sorter(path_for_sorting: str, path_for_sorting_2: list):
        if path_for_sorting_2:
            sort_targets([path_for_sorting, *path_for_sorting_2])
            return f"Folders {path_for_sorting} and {','.join(path_for_sorting_2)} successfully sorted."
        else:
            sort_targets(path_for_sorting)
            return f"Folder {path_for_sorting} successfully sorted."

    @staticmethod
    @erorr_catcher
    def create_path_for_saves() -> str:
        match platform:
            case "linux":
                abs_path = f"/home/{getlogin()}/Documents/help_you"
            case "win32":
                abs_path = f"C:/Users/{getlogin()}/AppData/Local/help_you"
            case "darwin":
                abs_path = f"Macintosh/Users/{getlogin()}/Documents/help_you"
            case _:
                raise OSError("I can't work with this OS. Sorry.")
        try:
            os.mkdir(abs_path)
            return abs_path
        except FileExistsError:
            return abs_path


def start():
    help_you = UserInterface()
    help_you.run()
start()