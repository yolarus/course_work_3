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

    def get_employers(self, query: list, top_n: int = 5) -> list:
        """
        Осуществляет поиск работодателей из списка запроса
        :param query: Запрашиваемый список работодателей
        :param top_n: Максимальное число найденных работодателей по одному запросу
        :return: Список работодателей
        """

        employers_list = []

        if self.get_status:
            for item in query:
                url = f"https://api.hh.ru/employers?text={item}&only_with_vacancies={True}"
                item_employers = requests.get(url).json()["items"]
                employers_list.extend(item_employers[:top_n] if len(item_employers) >= top_n
                                      else item_employers)

        return employers_list

    def get_vacancies_by_url(self, url: str) -> list:
        """
        Получение списка вакансий по ссылке
        :param url: ссылка на список вакансий
        :return: список подходящих вакансий
        """
        vacancies_list = []
        if self.get_status:
            vacancies_list = requests.get(f"{url}&only_with_salary={True}").json()["items"]
        return vacancies_list
