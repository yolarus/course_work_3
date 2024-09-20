from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """
    Абстрактный класс для работы с API поиска вакансий
    """

    @abstractmethod
    def get_status(self) -> bool:
        """
        Проверка подключения к API
        """
        pass

    @abstractmethod
    def get_employers(self, query: list, top_n: int) -> list:
        """
        Осуществляет поиск работодателей из списка запроса
        :param query: Запрашиваемый список работодателей
        :param top_n: Максимальное число найденных работодателей по одному запросу
        :return: Список работодателей
        """
        pass

    @abstractmethod
    def get_vacancies_by_url(self, url: str) -> list:
        """
        Получение списка вакансий по ссылке
        :param url: ссылка на список вакансий
        :return: список подходящих вакансий
        """
        pass
