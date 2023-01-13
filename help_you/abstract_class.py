from abc import abstractmethod, ABC
class WorkMethods(ABC):

    @abstractmethod
    def create(self):
        raise NotImplementedError

    @abstractmethod
    def add_value(self):
        raise NotImplementedError

    @abstractmethod
    def delete_all(self):
        raise NotImplementedError

    @abstractmethod
    def delete_one(self):
        raise NotImplementedError

    @abstractmethod
    def save_to_file(self):
        raise NotImplementedError

    @abstractmethod
    def load_from_file(self):
        raise NotImplementedError

    @abstractmethod
    def edit_information(self):
        raise NotImplementedError

    @abstractmethod
    def edit_name(self):
        raise NotImplementedError

    @abstractmethod
    def search_in(self):
        raise NotImplementedError


class InformationOutput(ABC):

    @abstractmethod
    def show_all(self):
        raise NotImplementedError

    @abstractmethod
    def show_one(self):
        raise NotImplementedError

    @abstractmethod
    def show_page(self):
        raise NotImplementedError