from typing import Any

import pytest

from src.db_manager import DBManager
from src.employer import Employer
from src.save_to_json_file import SaveToJSONFile
from src.save_to_postgreSQL import SaveToDBPostgreSQL
from src.vacancy import Vacancy


@pytest.fixture
def first_employer() -> Employer:
    """
    Фикстура - объект 1 класса Employer
    """
    result = Employer("Test",
                      "don't have",
                      "url_to_vacancies_list",
                      1)
    result.employer_id = 1
    return result


@pytest.fixture
def second_employer() -> Employer:
    """
    Фикстура - объект 2 класса Employer
    """
    result = Employer("Test",
                      "don't have",
                      "url_to_vacancies_list",
                      20)
    result.employer_id = 2
    return result


@pytest.fixture
def first_employer_dict() -> dict:
    """
    Фикстура - объект 1 класса Employer, преобразованный в словарь
    """
    return {"employer_id": 1,
            "name": "Test",
            "url": "don't have",
            "url_to_vacancies_list": "url_to_vacancies_list",
            "open_vacancies": 1}


@pytest.fixture
def second_employer_dict() -> dict:
    """
    Фикстура - объект 2 класса Employer, преобразованный в словарь
    """
    return {"employer_id": 2,
            "name": "Test",
            "url": "don't have",
            "url_to_vacancies_list": "url_to_vacancies_list",
            "open_vacancies": 20}


@pytest.fixture
def full_info_first_employer() -> dict:
    """
    Фикстура - работодатель 1, полученный с hh.ru в исходном формате
    """
    return {"name": "Test",
            "url": "don't have",
            "vacancies_url": "url_to_vacancies_list",
            "open_vacancies": 1}


@pytest.fixture
def full_info_second_employer() -> dict:
    """
    Фикстура - работодатель 2, полученный с hh.ru в исходном формате
    """
    return {"name": "Test",
            "url": "don't have",
            "vacancies_url": "url_to_vacancies_list",
            "open_vacancies": 25}


@pytest.fixture
def first_vacancy() -> Vacancy:
    """
    Фикстура - объект 1 класса Vacancy
    """
    result = Vacancy("Test",
                     "don't have",
                     {"from": 50000, "to": 100000, "currency": "RUR"},
                     "description",
                     "requirements",
                     "Москва")
    result.vacancy_id = 1
    return result


@pytest.fixture
def second_vacancy() -> Vacancy:
    """
    Фикстура - объект 2 класса Vacancy
    """
    result = Vacancy("Test 2",
                     "don't have",
                     {"from": 150000, "to": 200000, "currency": "RUR"},
                     "description",
                     "requirements",
                     "Можно не рассматривать данную вакансию")
    result.vacancy_id = 2
    return result


@pytest.fixture
def first_vacancy_dict() -> dict:
    """
    Фикстура - объект 1 класса Vacancy, преобразованный в словарь
    """
    return {"vacancy_id": 1,
            "employer_id": None,
            "name": "Test",
            "url": "don't have",
            "salary": {"from": 50000, "to": 100000, "currency": "RUR"},
            "short_description": "description",
            "requirements": "requirements",
            "area": "Москва"}


@pytest.fixture
def second_vacancy_dict() -> dict:
    """
    Фикстура - объект 2 класса Vacancy, преобразованный в словарь
    """
    return {"vacancy_id": 2,
            "employer_id": None,
            "name": "Test 2",
            "url": "don't have",
            "salary": {"from": 150000, "to": 200000, "currency": "RUR"},
            "short_description": "description",
            "requirements": "requirements",
            "area": "Можно не рассматривать данную вакансию"}


@pytest.fixture
def full_info_first_vacancy() -> dict:
    """
    Фикстура - вакансия 1, полученная с hh.ru в исходном формате
    """
    return {"name": "Test",
            "url": "don't have",
            "salary": {"from": 50000, "to": 100000, "currency": "RUR"},
            "snippet": {"responsibility": "description",
                        "requirement": "requirements"},
            "area": {"name": "Москва"}}


@pytest.fixture
def full_info_second_vacancy() -> dict:
    """
    Фикстура - вакансия 2, полученная с hh.ru в исходном формате
    """
    return {"name": "Test 2",
            "url": "don't have",
            "salary": {"from": 150000, "to": 200000, "currency": "RUR"},
            "snippet": {"responsibility": "description",
                        "requirement": "requirements"},
            "area": {"name": "Токио"}}


@pytest.fixture
def headers_vacancies() -> list:
    """
    Фикстура - список заголовков таблицы vacancies в БД
    """
    return ["vacancy_id int",
            "employer_id int",
            "name varchar(255)",
            "url varchar(255)",
            "salary_from int",
            "salary_to int",
            "salary_currency varchar(3)",
            "short_description text",
            "requirements text",
            "area varchar(255)"]


@pytest.fixture
def insert_data_first_vacancy() -> list:
    """
    Фикстура - выгрузка данных объекта 1 класса Vacancy
    """
    return [1,
            None,
            "Test",
            "don't have",
            50000,
            100000,
            "RUR",
            "description",
            "requirements",
            "Москва"]


@pytest.fixture
def headers_employers() -> list:
    """
    Фикстура - список заголовков таблицы employers в БД
    """
    return ["employer_id int",
            "name varchar(255)",
            "url varchar(255)",
            "url_to_vacancies_list varchar(255)",
            "open_vacancies int"]


@pytest.fixture
def insert_data_first_employer() -> list:
    """
    Фикстура - выгрузка данных объекта 1 класса Employer
    """
    return [1,
            "Test",
            "don't have",
            "url_to_vacancies_list",
            1]


@pytest.fixture
def saver_json() -> SaveToJSONFile:
    """
    Фикстура - объект класса SaveToJSONFile
    """
    return SaveToJSONFile("test_data/test")


@pytest.fixture
def reset_vacancies_and_employers_id() -> None:
    """
    Фикстура - обнуление ID классов Vacancy и Employer
    :return: None
    """
    Vacancy.ID = 0
    Employer.ID = 0


@pytest.fixture
def postgre_saver_create_db() -> None:
    """
    Фикстура - создание БД
    :return: None
    """
    result = SaveToDBPostgreSQL()
    result.create_db("alyautdinov_rt_cw_3_test")


@pytest.fixture
def postgre_saver_create_table(first_vacancy: Vacancy,
                               first_employer: Employer) -> None:
    """
    Фикстура - создание таблиц в БД
    :return: None
    """
    result = SaveToDBPostgreSQL()
    result.create_table("vacancies",
                        first_vacancy.get_headers_to_db(),
                        "alyautdinov_rt_cw_3_test")
    result.create_table("employers",
                        first_employer.get_headers_to_db(),
                        "alyautdinov_rt_cw_3_test")


@pytest.fixture
def postgre_saver_fill_table(first_vacancy: Vacancy,
                             second_vacancy: Vacancy,
                             first_employer: Employer,
                             second_employer: Employer) -> None:
    """
    Фикстура - заполнение таблиц в БД
    :return: None
    """
    first_vacancy.employer_id = 2
    second_vacancy.employer_id = 1

    result = SaveToDBPostgreSQL()
    result.fill_table("vacancies",
                      [first_vacancy.get_insert_data_to_db(), second_vacancy.get_insert_data_to_db()],
                      "alyautdinov_rt_cw_3_test")
    result.fill_table("employers",
                      [first_employer.get_insert_data_to_db(), second_employer.get_insert_data_to_db()],
                      "alyautdinov_rt_cw_3_test")


@pytest.fixture
def postgre_saver_add_pk() -> None:
    """
    Фикстура - создание PRIMARY KEY в таблицах БД
    :return: None
    """
    result = SaveToDBPostgreSQL()
    result.add_pk_to_table("vacancies",
                           "vacancy_id",
                           "alyautdinov_rt_cw_3_test")
    result.add_pk_to_table("employers",
                           "employer_id",
                           "alyautdinov_rt_cw_3_test")


@pytest.fixture
def postgre_saver_add_fk() -> None:
    """
    Фикстура - создание FOREIGN KEY в таблице БД
    :return: None
    """
    result = SaveToDBPostgreSQL()
    result.add_fk_to_table("vacancies",
                           "employer_id",
                           "employers",
                           "employer_id",
                           "alyautdinov_rt_cw_3_test")


@pytest.fixture
def previously_on_postgre_manager(postgre_saver_create_db: Any,
                                  postgre_saver_create_table: Any,
                                  postgre_saver_fill_table: Any,
                                  postgre_saver_add_pk: Any,
                                  postgre_saver_add_fk: Any) -> None:
    """
    Фикстура - Создание и заполнение БД
    :return: None
    """
    pass


@pytest.fixture
def postgre_manager() -> DBManager:
    """
    Фикстура - объект DBManager - для выборки данных из БД
    :return: объект DBManager
    """
    return DBManager()
