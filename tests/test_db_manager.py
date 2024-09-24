from typing import Any
from unittest.mock import patch

from src.db_manager import DBManager


def test_db_manager_get_companies_and_vacancies_count(previously_on_postgre_manager: Any,
                                                      postgre_manager: DBManager) -> None:
    """
    Тест метода получения списка всех компаний и количества вакансий у каждой компании
    """

    result = postgre_manager.get_companies_and_vacancies_count("alyautdinov_rt_cw_3_test")

    assert result == [("Test", 1), ("Test", 20)]


def test_db_manager_get_companies_and_vacancies_count_error(previously_on_postgre_manager: Any,
                                                            postgre_manager: DBManager,
                                                            capsys: Any) -> None:
    """
    Тест метода получения списка всех компаний и количества вакансий у каждой компании с ошибкой
    """
    with patch("psycopg2.connect", side_effect=Exception('Ошибка соединения с БД')):
        postgre_manager.get_companies_and_vacancies_count("test")
        message = capsys.readouterr()
        assert message.out.split("\n")[0] == "Ошибка при работе с PostgreSQL: Ошибка соединения с БД"


def test_db_manager_get_all_vacancies(previously_on_postgre_manager: Any,
                                      postgre_manager: DBManager) -> None:
    """
    Тест метода получения списка всех вакансий
    """

    result = postgre_manager.get_all_vacancies("alyautdinov_rt_cw_3_test")

    assert result == [("Test", "Test", 50000, 100000, "RUR", "don't have"),
                      ("Test", "Test 2", 150000, 200000, "RUR", "don't have")]


def test_db_manager_get_all_vacancies_error(previously_on_postgre_manager: Any,
                                            postgre_manager: DBManager,
                                            capsys: Any) -> None:
    """
    Тест метода получения списка всех вакансий с ошибкой
    """
    with patch("psycopg2.connect", side_effect=Exception('Ошибка соединения с БД')):
        postgre_manager.get_all_vacancies("test")
        message = capsys.readouterr()
        assert message.out.split("\n")[0] == "Ошибка при работе с PostgreSQL: Ошибка соединения с БД"


def test_db_manager_get_avg_salary(previously_on_postgre_manager: Any,
                                   postgre_manager: DBManager) -> None:
    """
    Тест метода получения средней зарплаты по вакансиям в заданной валюте
    """

    result = postgre_manager.get_avg_salary(db_name="alyautdinov_rt_cw_3_test")

    assert result == "125000.00 RUR"


def test_db_manager_get_avg_salary_error(previously_on_postgre_manager: Any,
                                         postgre_manager: DBManager,
                                         capsys: Any) -> None:
    """
    Тест метода получения средней зарплаты по вакансиям в заданной валюте с ошибкой
    """
    with patch("psycopg2.connect", side_effect=Exception('Ошибка соединения с БД')):
        postgre_manager.get_avg_salary("test")
        message = capsys.readouterr()
        assert message.out.split("\n")[0] == "Ошибка при работе с PostgreSQL: Ошибка соединения с БД"


def test_db_manager_get_vacancies_with_higher_salary(previously_on_postgre_manager: Any,
                                                     postgre_manager: DBManager) -> None:
    """
    Тест метода получения списка вакансий с зарплатой выше среднего
    """

    result = postgre_manager.get_vacancies_with_higher_salary(db_name="alyautdinov_rt_cw_3_test")

    assert result == [("Test", "Test 2", 150000, 200000, "RUR", "don't have")]


def test_db_manager_get_vacancies_with_higher_salary_error(previously_on_postgre_manager: Any,
                                                           postgre_manager: DBManager,
                                                           capsys: Any) -> None:
    """
    Тест метода получения списка вакансий с зарплатой выше среднего с ошибкой
    """
    with patch("psycopg2.connect", side_effect=Exception('Ошибка соединения с БД')):
        postgre_manager.get_vacancies_with_higher_salary(db_name="test")
        message = capsys.readouterr()
        assert message.out.split("\n")[0] == "Ошибка при работе с PostgreSQL: Ошибка соединения с БД"


def test_db_manager_get_vacancies_with_keyword(previously_on_postgre_manager: Any,
                                               postgre_manager: DBManager) -> None:
    """
    Тест метода получения списка вакансий по ключевому слову в названии
    """

    result = postgre_manager.get_vacancies_with_keyword(keyword="2",
                                                        db_name="alyautdinov_rt_cw_3_test")

    assert result == [("Test", "Test 2", 150000, 200000, "RUR", "don't have")]


def test_db_manager_get_vacancies_with_keyword_error(previously_on_postgre_manager: Any,
                                                     postgre_manager: DBManager,
                                                     capsys: Any) -> None:
    """
    Тест метода получения списка вакансий по ключевому слову в названии с ошибкой
    """
    with patch("psycopg2.connect", side_effect=Exception('Ошибка соединения с БД')):
        postgre_manager.get_vacancies_with_keyword("2", "test")
        message = capsys.readouterr()
        assert message.out.split("\n")[0] == "Ошибка при работе с PostgreSQL: Ошибка соединения с БД"
