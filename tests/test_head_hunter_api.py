from typing import Any
from unittest.mock import patch

from src.employer import Employer
from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy


@patch("requests.get")
def test_head_hunter_api_get_status(mock_get: Any) -> None:
    """
    Тест подключения к hh.ru
    """
    mock_get.return_value.status_code = 200
    test = HeadHunterAPI()
    assert test.get_status is True


@patch("requests.get")
def test_head_hunter_api_get_status_error(mock_get: Any) -> None:
    """
    Тест подключения к hh.ru с ошибкой
    """
    mock_get.return_value.status_code = 404
    test = HeadHunterAPI()
    assert test.get_status is False


@patch("requests.get")
@patch("src.head_hunter_api.HeadHunterAPI.get_status")
def test_head_hunter_api_get_employers(mock_get_status: Any,
                                       mock_get_employers: Any,
                                       first_employer: Employer) -> None:
    """
    Тест получения списка работодателей с hh.ru
    """
    mock_get_status.return_value = True
    mock_get_employers.return_value.json.return_value = {"items": [first_employer]}
    test = HeadHunterAPI()

    assert test.get_employers(["Яндекс"]) == [first_employer]


@patch("requests.get")
def test_head_hunter_api_get_employers_error(mock_get_status: Any) -> None:
    """
    Тест получения списка работодателей с hh.ru с ошибкой
    """
    mock_get_status.return_value.status_code = 404
    test = HeadHunterAPI()
    assert test.get_employers(["Яндекс"]) == []


@patch("requests.get")
@patch("src.head_hunter_api.HeadHunterAPI.get_status")
def test_head_hunter_api_get_vacancies_by_url(mock_get_status: Any,
                                              mock_get_vacancies: Any,
                                              first_vacancy: Vacancy) -> None:
    """
    Тест получения списка вакансий с hh.ru
    """
    mock_get_status.return_value = True
    mock_get_vacancies.return_value.json.return_value = {"items": [first_vacancy]}
    test = HeadHunterAPI()

    assert test.get_vacancies_by_url("url") == [first_vacancy]


@patch("requests.get")
def test_head_hunter_api_get_vacancies_by_url_error(mock_get_status: Any) -> None:
    """
    Тест получения списка вакансий с hh.ru с ошибкой
    """
    mock_get_status.return_value.status_code = 404
    test = HeadHunterAPI()
    assert test.get_vacancies_by_url("url") == []
