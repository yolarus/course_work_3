from src.db_manager import DBManager
from src.employer import Employer
from src.head_hunter_api import HeadHunterAPI
from src.save_to_json_file import SaveToJSONFile
from src.save_to_postgreSQL import SaveToDBPostgreSQL
from src.utils import list_of_employers, list_of_vacancies
from src.vacancy import Vacancy


def user_interaction() -> None:
    """
    Функция для взаимодействия с пользователем
    """

    # Получение данных для запроса от пользователя

    print("Добро пожаловать в программу для поиска ваканси от любимых компаний! ")
    search_query = input("Если вы не знаете какие компании выбрать нажмите ENTER и "
                         "поиск будет осуществляться среди самых популярных.\n"
                         "Если знаете - введите названия компаний через пробел: ")  # Яндекс
    top_n = int(input("Введите максимальное количество компаний (до 100) подходящих под каждый запрос: "))  # 2

    if search_query:
        query = search_query.split()
    else:
        query = ["Сбер", "Яндекс", "Т-банк", "VK"]

    # Выполнение запроса поиска подходящих компаний
    head_hunter_api = HeadHunterAPI()
    employers_list = list_of_employers(head_hunter_api.get_employers(query, top_n))

    # Выполнение запроса поиска вакансий у подходящих компаний
    vacancies_list = []
    for employer in employers_list:
        employer_vacancies = list_of_vacancies(
            head_hunter_api.get_vacancies_by_url(employer.url_to_vacancies_list),
            employer.employer_id)
        vacancies_list.extend(employer_vacancies)

    # Сохранение найденных компаний в json файл
    employer_json_saver = SaveToJSONFile("employers")
    employer_json_saver.clear_file()
    for employer in employers_list:
        employer_json_saver.add_to_file(employer)
    print("Работодатели выгружены в файл: data/employers.json")

    # Сохранение найденных вакансий в json файл
    vacancies_json_saver = SaveToJSONFile("vacancies")
    vacancies_json_saver.clear_file()
    for vacancy in vacancies_list:
        vacancies_json_saver.add_to_file(vacancy)
    print("Вакансии выгружены в файл: data/vacancies.json")

    # Создание БД
    save_to_postgres = SaveToDBPostgreSQL()
    save_to_postgres.create_db("alyautdinov_rt_cw_3")
    print("Создана БД alyautdinov_rt_cw_3")

    # Создание и заполнение таблицы компаний в БД
    save_to_postgres.create_table("employers", Employer.get_headers_to_db())
    save_to_postgres.fill_table("employers", [employer.get_insert_data_to_db() for employer in employers_list])
    save_to_postgres.add_pk_to_table("employers", "employer_id")
    print("Данные о компаниях занесены в таблицу employers БД")

    # Создание и заполнение таблицы вакансий в БД
    save_to_postgres.create_table("vacancies", Vacancy.get_headers_to_db())
    save_to_postgres.fill_table("vacancies", [vacancy.get_insert_data_to_db() for vacancy in vacancies_list])
    save_to_postgres.add_pk_to_table("vacancies", "vacancy_id")
    save_to_postgres.add_fk_to_table("vacancies", "employer_id", "employers", "employer_id")
    print("Данные о вакансиях занесены в таблицу vacancies БД")

    # Вывод различных запросов к БД
    db_manager = DBManager()

    print("Под ваш запрос подходят следующие компании:")
    print(db_manager.get_companies_and_vacancies_count())

    print("Данные о всех вакансиях:")
    print(db_manager.get_all_vacancies())

    currency = input("Введите код валюты для расчета средней зарплаты по найденным вакансиям (пример - RUR): ")  # RUR
    print("Средняя зарплата по данной выборке составляет:")
    print(db_manager.get_avg_salary(currency))

    print("Данные по вакансиям, у которых зарплата выше средней:")
    print(db_manager.get_vacancies_with_higher_salary(currency))

    keyword = input("Введите ключевое слово для поиска по названию вакансии: ")  # Менеджер
    print("Вашему запросу удовлетворяют следующие варианты:")
    print(db_manager.get_vacancies_with_keyword(keyword))


if __name__ == "__main__":
    user_interaction()
