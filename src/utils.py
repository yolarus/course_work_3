from typing import Optional

from src.employer import Employer
from src.save_to_json_file import SaveToJSONFile
from src.vacancy import Vacancy


def list_of_vacancies(full_info_vacancies: list, employer_id: Optional[int] = None) -> list[Vacancy]:
    """
    Функция для преобразования списка вакансий из hh.ru в список объектов Vacancy
    :param full_info_vacancies: список вакансий из hh.ru с полной информацией
    :param employer_id: опциональный параметр для присвоения локального id работодателя
    :return: список вакансий преобразованных в класс Vacancy
    """
    result = []
    for item in full_info_vacancies:
        new_vacancy = Vacancy(item["name"],
                              item["url"],
                              {"from": int(item["salary"]["from"])
                              if item["salary"]["from"]
                              else item["salary"]["to"],
                               "to": int(item["salary"]["to"])
                               if item["salary"]["to"]
                               else int(item["salary"]["from"]),
                               "currency": item["salary"]["currency"]},
                              item["snippet"]["responsibility"],
                              item["snippet"]["requirement"],
                              item["area"]["name"])
        if employer_id:
            new_vacancy.employer_id = employer_id
        result.append(new_vacancy)
    return result


def list_of_employers(full_info_employers: list) -> list[Employer]:
    """
    Функция для преобразования списка работадателей из hh.ru в список объектов Employer
    :param full_info_employers: список работадателей из hh.ru с полной информацией
    :return: список работадателей преобразованных в класс Employer
    """
    result = []
    for item in full_info_employers:
        result.append(Employer(item["name"],
                               item["url"],
                               item["vacancies_url"],
                               item["open_vacancies"] if item["open_vacancies"] <= 20 else 20))
    return result


def use_to_list_json_saver(items: list, file_name: str) -> None:
    """
    Функция для быстрого сохранения через класс SaveToJSONFile списка объектов
    :param items: Список объектов для сохранения
    :param file_name: Имя файла для сохранения данных
    :return: None
    """

    item_json_saver = SaveToJSONFile(file_name)
    item_json_saver.clear_file()
    for item in items:
        item_json_saver.add_to_file(item)
    print(f"Данные выгружены в файл: data/{file_name}.json")
