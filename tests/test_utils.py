import json
from typing import Any

from src.utils import list_of_employers, list_of_vacancies, use_to_list_json_saver
from src.vacancy import Vacancy


def test_list_of_vacancies(full_info_first_vacancy: dict,
                           full_info_second_vacancy: dict,
                           first_vacancy: Vacancy,
                           second_vacancy: Vacancy,
                           reset_vacancies_and_employers_id: Any) -> None:
    """
    Тестирование функции преобразования списка вакансий из hh.ru в список объектов Vacancy
    """
    result = list_of_vacancies([full_info_first_vacancy, full_info_second_vacancy], 3)
    first_vacancy.employer_id = 3
    second_vacancy.employer_id = 3
    assert result[0].to_dict() == first_vacancy.to_dict()
    assert result[1].to_dict() == second_vacancy.to_dict()


def test_list_of_employers(full_info_first_employer: dict,
                           full_info_second_employer: dict,
                           first_employer_dict: dict,
                           second_employer_dict: dict,
                           reset_vacancies_and_employers_id: Any) -> None:
    """
    Тестирование функции преобразования списка работодателей из hh.ru в список объектов Vacancy
    """
    result = list_of_employers([full_info_first_employer, full_info_second_employer])
    assert result[0].to_dict() == first_employer_dict
    assert result[1].to_dict() == second_employer_dict


def test_use_to_list_json_saver(first_vacancy: Vacancy,
                                second_vacancy: Vacancy,
                                first_vacancy_dict: dict,
                                second_vacancy_dict: dict) -> None:
    """
    Тестирование функции сохранения через класс SaveToJSONFile списка объектов
    """
    use_to_list_json_saver([first_vacancy, second_vacancy], "test_data/test_list")

    with open("data/test_data/test_list.json", "r") as f:
        data = json.load(f)
    assert data == [first_vacancy_dict, second_vacancy_dict]
