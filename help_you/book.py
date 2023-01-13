from collections import UserDict
import pickle
class Book(UserDict):
    def __init__(self, file_path):
        super().__init__()
        self.path_to_save = file_path

    def iterator(self, n: int) -> list:
        """Пагінація - посторінковий вивід Контактної книги """
        page = []
        for i in self.data.keys():
            page.append(i)
            if len(page) == n:
                yield page
                page = []
        if page:
            yield page

    def save_to_file(self):
        """Збереження Книги контактів у бінарний файл """

        with open(self.path_to_save, "wb") as file:
            pickle.dump(self.data, file)
        return f"Book saved in '{self.path_to_save}'"

    def load_from_file(self):
        """Завантаження Книги контактів з бінарного файлу """

        with open(self.path_to_save, "rb") as file:
            self.data = pickle.load(file)
        return f"Book loaded from '{self.path_to_save}'"
