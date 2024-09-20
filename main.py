from src.head_hunter_api import HeadHunterAPI
from src.utils import list_of_vacancies, list_of_employers, print_vacancies
from src.save_to_postgreSQL import SaveToDBPostgreSQL


def user_interaction() -> None:
    """
    Функция для взаимодействия с пользователем
    """

    head_hunter_api = HeadHunterAPI()
    employers_list = list_of_employers(head_hunter_api.get_employers(["Яндекс"]))

    vacancies_list = []
    for employer in employers_list:
        employer_vacancies = list_of_vacancies(
            head_hunter_api.get_vacancies_by_url(employer.url_to_vacancies_list),
            employer.employer_id)
        vacancies_list.extend(employer_vacancies)

    print_vacancies(vacancies_list, 50)
    # vacancies_urls = head_hunter_api.get_vacancies_urls([])
    #
    # vacancies_full_info_list = []
    # for vacancy_url in vacancies_urls:
    #     vacancies_full_info_list.extend(head_hunter_api.get_vacancies_by_url(vacancy_url))
    #
    # vacancies = list_of_vacancies(vacancies_full_info_list)

    # result = print_vacancies(vacancies, 25)


    #
    # saver_json = SaveToJSONFile()
    # saver_json.clear_file()
    # for item in result:
    #     saver_json.add_to_file(item)
    # print("Ваши вакансии выгружены в файл: data/vacancies.json")


if __name__ == "__main__":
    user_interaction()
    # test = SaveToDBPostgreSQL()
    # test.create_db("alyautdinov_rt_cw_3")
    # test.create_table("test", ["id serial", "payment int"])
    # test.fill_table("test", [[1, 10000], [2, 20000]])
