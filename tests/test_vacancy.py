from src.vacancy import Vacancy


def test_vacancy_str(first_vacancy: Vacancy) -> None:
    """
    Тест пользовательского отображения для класса Vacancy
    """
    first_vacancy.employer_id = 1
    assert str(first_vacancy) == ("ID: 1 -- ID работодателя: 1 -- Test -- don't have\n"
                                  "Зарплата: от 50000 до 100000 RUR\n"
                                  "Краткое описание: description\n"
                                  "Требования: requirements\n"
                                  "Место работы: Москва\n")


def test_vacancy__eq__(first_vacancy: Vacancy, second_vacancy: Vacancy) -> None:
    """
    Тест метода равенства для класса Vacancy
    """
    assert (first_vacancy == first_vacancy) is True
    assert (first_vacancy == second_vacancy) is False


def test_vacancy__lt__le__(first_vacancy: Vacancy, second_vacancy: Vacancy) -> None:
    """
    Тест методов меньше и меньше или равно для класса Vacancy
    """
    assert (first_vacancy < second_vacancy) is True
    assert (first_vacancy > second_vacancy) is False
    assert (first_vacancy <= second_vacancy) is True
    assert (first_vacancy >= second_vacancy) is False


def test_vacancy__check_city(first_vacancy: Vacancy, second_vacancy: Vacancy) -> None:
    """
    Тест валидации места работы для класса Vacancy
    """
    assert first_vacancy.area == "Москва"
    assert second_vacancy.area == "Можно не рассматривать данную вакансию"


def test_vacancy_to_dict(first_vacancy: Vacancy,
                         first_vacancy_dict: dict) -> None:
    """
    Тест преобразования в словарь для класса Vacancy
    """
    assert first_vacancy.to_dict() == first_vacancy_dict


def test_vacancy_get_headers_to_db(first_vacancy: Vacancy,
                                   headers_vacancies: list) -> None:
    """
    Тест получения списка заголовков столбцов для загрузки данных в БД
    """

    assert first_vacancy.get_headers_to_db() == headers_vacancies


def test_vacancy_get_insert_data_to_db(first_vacancy: Vacancy,
                                       insert_data_first_vacancy: list) -> None:
    """
    Тест получения данных для заполнения таблиц в БД
    """
    assert first_vacancy.get_insert_data_to_db() == insert_data_first_vacancy
