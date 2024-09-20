from abc import ABC, abstractmethod
from typing import Any

from src.employer import Employer
from src.vacancy import Vacancy


class SaveToFile(ABC):
    """
    Абстрактный класс для работы с объектами класса Vacancy, Employer и файлами различного формата
    """
    @abstractmethod
    def save_to_file(self, item: Vacancy | Employer) -> None:
        """
        Абстрактный метод для сохранения объекта класса Vacancy, Employer в новый файл/ перезаписи файла
        """
        pass

    @abstractmethod
    def read_from_file(self) -> Any:
        """
        Абстрактный метод для получения списка объектов класса Vacancy, Employer из файла
        """
        pass

    @abstractmethod
    def add_to_file(self, item: Vacancy | Employer) -> None:
        """
        Абстрактный метод для добавления объекта класса Vacancy, Employer в файл
        """
        pass

    @abstractmethod
    def delete_from_file(self, item: Vacancy | Employer) -> None:
        """
        Абстрактный метод для удаления объекта класса Vacancy, Employer из файла
        """
        pass
