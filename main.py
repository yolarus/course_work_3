from src.db_manager import DBManager
from src.employer import Employer
from src.head_hunter_api import HeadHunterAPI
from src.save_to_postgreSQL import SaveToDBPostgreSQL
from src.utils import list_of_employers, list_of_vacancies
from src.vacancy import Vacancy


def user_interaction() -> None:
    """
    Функция для взаимодействия с пользователем
    """

    head_hunter_api = HeadHunterAPI()
    employers_list = list_of_employers(head_hunter_api.get_employers(["Яндекс"], 2))

    vacancies_list = []
    for employer in employers_list:
        employer_vacancies = list_of_vacancies(
            head_hunter_api.get_vacancies_by_url(employer.url_to_vacancies_list),
            employer.employer_id)
        vacancies_list.extend(employer_vacancies)

    save_to_postgres = SaveToDBPostgreSQL()
    save_to_postgres.create_db("alyautdinov_rt_cw_3")

    save_to_postgres.create_table("employers", Employer.get_headers_to_db())
    save_to_postgres.fill_table("employers", [employer.get_insert_data_to_db() for employer in employers_list])
    save_to_postgres.add_pk_to_table("employers", "employer_id")

    save_to_postgres.create_table("vacancies", Vacancy.get_headers_to_db())
    save_to_postgres.fill_table("vacancies", [vacancy.get_insert_data_to_db() for vacancy in vacancies_list])
    save_to_postgres.add_pk_to_table("vacancies", "vacancy_id")
    save_to_postgres.add_fk_to_table("vacancies", "employer_id", "employers", "employer_id")

    db_manager = DBManager()
    print(db_manager.get_companies_and_vacancies_count())
    print(db_manager.get_all_vacancies())
    print(db_manager.get_avg_salary())
    print(db_manager.get_vacancies_with_higher_salary())
    print(db_manager.get_vacancies_with_keyword("Менеджер"))


if __name__ == "__main__":
    user_interaction()
    # test = SaveToDBPostgreSQL()
    # test.create_db("alyautdinov_rt_cw_3")
    # test.create_table("test", ["id serial", "payment varchar", "test varchar", "test_2 varchar"])
    # test.fill_table("test", [[1, "10000", "test", "test"], [2, "20000", "test", "test"]])
