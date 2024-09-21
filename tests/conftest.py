import pytest

from src.save_to_json_file import SaveToJSONFile
from src.vacancy import Vacancy
from src.employer import Employer


@pytest.fixture
def first_employer() -> Employer:
    """
    Фикстура - объект 1 класса Employer
    """
    return Employer("Test",
                    "don't have",
                    "url_to_vacancies_list",
                    1)


@pytest.fixture
def second_employer() -> Employer:
    """
    Фикстура - объект 2 класса Employer
    """
    return Employer("Test",
                    "don't have",
                    "url_to_vacancies_list",
                    25)


@pytest.fixture
def first_vacancy() -> Vacancy:
    """
    Фикстура - объект 1 класса Vacancy
    """
    return Vacancy("Test",
                   "don't have",
                   {"from": 50000, "to": 100000, "currency": "RUR"},
                   "description",
                   "requirements",
                   "Москва")


@pytest.fixture
def second_vacancy() -> Vacancy:
    """
    Фикстура - объект 2 класса Vacancy
    """
    return Vacancy("Test 2",
                   "don't have",
                   {"from": 150000, "to": 200000, "currency": "RUR"},
                   "description",
                   "requirements",
                   "Токио")


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
def full_info_first_vacancy_dict() -> dict:
    """
    Фикстура - объект 1 класса Vacancy, преобразованный в словарь
    """
    return {"name": "Test",
            "url": "don't have",
            "salary": {"from": 50000, "to": 100000, "currency": "RUR"},
            "snippet": {"responsibility": "description",
                        "requirement": "requirements"},
            "area": {"name": "Москва"}}


@pytest.fixture
def full_info_second_vacancy_dict() -> dict:
    """
    Фикстура - объект 2 класса Vacancy, преобразованный в словарь
    """
    return {"name": "Test 2",
            "url": "don't have",
            "salary": {"from": 150000, "to": 200000, "currency": "RUR"},
            "snippet": {"responsibility": "description",
                        "requirement": "requirements"},
            "area": {"name": "Москва"}}


@pytest.fixture
def saver_json() -> SaveToJSONFile:
    """
    Фикстура - объект класса SaveToJSONFile
    """
    return SaveToJSONFile("test_data/test")


@pytest.fixture
def reset_vacancies_and_employers_id() -> None:
    """
    Фикстура - обнуление id вакансий и компаний в классах Vacancy и Employer
    :return: None
    """
    Vacancy.ID = 0
    Employer.ID = 0


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
