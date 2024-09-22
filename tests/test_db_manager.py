import os
from typing import Any

from dotenv import load_dotenv

from src.db_manager import DBManager

load_dotenv(".env")
password_to_postgres = os.getenv("PASSWORD_TO_POSTGRES")


def test_db_manager_get_companies_and_vacancies_count(postgre_saver_create_db: Any,
                                                      postgre_saver_create_table: Any,
                                                      postgre_saver_fill_table: Any,
                                                      postgre_saver_add_pk: Any,
                                                      postgre_saver_add_fk: Any,
                                                      postgre_manager: DBManager) -> None:
    """
    Тест метода получения списка всех компаний и количества вакансий у каждой компании
    """

    result = postgre_manager.get_companies_and_vacancies_count("alyautdinov_rt_cw_3_test")

    assert result == [("Test", 1), ("Test", 20)]


def test_db_manager_get_all_vacancies(postgre_saver_create_db: Any,
                                      postgre_saver_create_table: Any,
                                      postgre_saver_fill_table: Any,
                                      postgre_saver_add_pk: Any,
                                      postgre_saver_add_fk: Any,
                                      postgre_manager: DBManager) -> None:
    """
    Тест метода получения списка всех вакансий
    """

    result = postgre_manager.get_all_vacancies("alyautdinov_rt_cw_3_test")

    assert result == [("Test", "Test", 50000, 100000, "RUR", "don't have"),
                      ("Test", "Test 2", 150000, 200000, "RUR", "don't have")]


def test_db_manager_get_avg_salary(postgre_saver_create_db: Any,
                                   postgre_saver_create_table: Any,
                                   postgre_saver_fill_table: Any,
                                   postgre_saver_add_pk: Any,
                                   postgre_saver_add_fk: Any,
                                   postgre_manager: DBManager) -> None:
    """
    Тест метода получения средней зарплаты по вакансиям в заданной валюте
    """

    result = postgre_manager.get_avg_salary(db_name="alyautdinov_rt_cw_3_test")

    assert result == "125000.00 RUR"


def test_db_manager_get_vacancies_with_higher_salary(postgre_saver_create_db: Any,
                                                     postgre_saver_create_table: Any,
                                                     postgre_saver_fill_table: Any,
                                                     postgre_saver_add_pk: Any,
                                                     postgre_saver_add_fk: Any,
                                                     postgre_manager: DBManager) -> None:
    """
    Тест метода получения списка вакансий с зарплатой выше среднего
    """

    result = postgre_manager.get_vacancies_with_higher_salary(db_name="alyautdinov_rt_cw_3_test")

    assert result == [("Test", "Test 2", 150000, 200000, "RUR", "don't have")]


def test_db_manager_get_vacancies_with_keyword(postgre_saver_create_db: Any,
                                               postgre_saver_create_table: Any,
                                               postgre_saver_fill_table: Any,
                                               postgre_saver_add_pk: Any,
                                               postgre_saver_add_fk: Any,
                                               postgre_manager: DBManager) -> None:
    """
    Тест метода получения списка вакансий по ключевому слову в названии
    """

    result = postgre_manager.get_vacancies_with_keyword(keyword="2",
                                                        db_name="alyautdinov_rt_cw_3_test")

    assert result == [("Test", "Test 2", 150000, 200000, "RUR", "don't have")]
