import json
from typing import Any

from src.base_save_to_file import SaveToFile
from src.employer import Employer
from src.vacancy import Vacancy


class SaveToJSONFile(SaveToFile):
    """
    Класс для работы с объектами класса Vacancy, Employer и файлом формата json
    """
    __file_name: str

    def __init__(self, file_name: str) -> None:
        self.__file_name = file_name

    def save_to_file(self, item: Vacancy | Employer) -> None:
        """
        Метод для сохранения объекта класса Vacancy, Employer
        в новый файл формата .json/ перезаписи файла формата .json
        """
        data = [item.to_dict()]
        with open(f"data/{self.__file_name}.json", "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def read_from_file(self) -> Any:
        """
        Метод для получения списка объектов класса Vacancy, Employer из файла формата .json
        """
        with open(f"data/{self.__file_name}.json", "r", encoding="UTF-8") as file:
            data = json.load(file)
        return data

    def add_to_file(self, item: Vacancy | Employer) -> None:
        """
        Метод для добавления объекта класса Vacancy, Employer в файл формата .json
        """
        data = self.read_from_file()
        if item.to_dict() not in data:
            data.append(item.to_dict())
        with open(f"data/{self.__file_name}.json", "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def delete_from_file(self, item: Vacancy | Employer) -> None:
        """
        Метод для удаления объекта класса Vacancy, Employer из файла формата .json
        """
        data = self.read_from_file()

        for index, element in enumerate(data):
            if element == item.to_dict():
                data.pop(index)

        with open(f"data/{self.__file_name}.json", "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def clear_file(self) -> None:
        with open(f"data/{self.__file_name}.json", "w", encoding="UTF-8") as file:
            json.dump([], file)
