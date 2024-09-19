import requests

from src.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    """
    Класс для получения вакансий с headhunter.ru
    """
    __connection: bool

    @property
    def get_status(self) -> bool:  # type: ignore[override]
        """
        Проверка подключения к headhunter.ru
        """
        if requests.get("https://api.hh.ru/vacancies").status_code == 200:
            self.__connection = True
        else:
            self.__connection = False
        return self.__connection

    def get_vacancies_urls(self, query: list, top_n: int = 5) -> list:
        """
        Осуществляет поиск работаделей из списка запроса и возвращает список ссылок на вакансии найденных работадателей
        :param query: Запрашиваемые список работадателей
        :param top_n: Максимальное число найденных работадателей по одному запросу
        :return: Список ссылок на вакансии работадателей
        """
        if not query:
            query = ["Сбер", "Яндекс"]

        vacancies_urls_list = []

        if self.get_status:
            for item in query:
                url = f"https://api.hh.ru/employers?text={item}&only_with_vacancies={True}"
                item_vacancies = requests.get(url).json()["items"]
                item_vacancies_urls = [vacancy["vacancies_url"] for vacancy in item_vacancies]
                vacancies_urls_list.extend(item_vacancies_urls[:top_n] if len(item_vacancies_urls) >= top_n
                                           else item_vacancies_urls)

        return vacancies_urls_list

    def get_vacancies_by_url(self, url: str) -> list:
        """
        Получение списка вакансий по ссылке
        :param url: ссылка на список вакансий
        :return: список подходящих вакансий
        """
        if self.get_status:
            vacancies_list = requests.get(f"{url}&only_with_salary={True}").json()["items"]
        else:
            vacancies_list = []
        return vacancies_list

    def get_vacancies_by_query(self, query: str, per_page: int = 100) -> list:
        """
        Поиск вакансий по ключевому слову
        :param query: поисковой запрос
        :param per_page: максимальное количество вакансий
        :return: список подходящих вакансий
        """
        if self.get_status:
            url = f"https://api.hh.ru/vacancies?text={query}&per_page={per_page}&only_with_salary={True}"
            vacancies_list = requests.get(url).json()["items"]
        else:
            vacancies_list = []
        return vacancies_list
