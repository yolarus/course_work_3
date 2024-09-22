from src.employer import Employer


def test_employer_str(first_employer: Employer) -> None:
    """
    Тест пользовательского отображения для класса Employer
    """
    assert str(first_employer) == ("ID: 1 -- Test -- don't have\n"
                                   "Доступные вакансии: url_to_vacancies_list\n"
                                   "Всего открытых вакансий: 1\n")


def test_employer_to_dict(first_employer: Employer,
                          first_employer_dict: dict) -> None:
    """
    Тест преобразования в словарь для класса Vacancy
    """
    assert first_employer.to_dict() == first_employer_dict


def test_employer_get_headers_to_db(first_employer: Employer,
                                    headers_employers: list) -> None:
    """
    Тест получения списка заголовков столбцов для загрузки данных в БД
    """
    assert first_employer.get_headers_to_db() == headers_employers


def test_employer_get_insert_data_to_db(first_employer: Employer,
                                        insert_data_first_employer: list) -> None:
    """
    Тест получения данных для заполнения таблиц в БД
    """
    assert first_employer.get_insert_data_to_db() == insert_data_first_employer
