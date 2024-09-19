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
    def get_vacancies_by_url(self, url: str) -> list:
        """
        Получение списка вакансий по ссылке
        :param url: ссылка на список вакансий
        :return: список подходящих вакансий
        """
        pass

    @abstractmethod
    def get_vacancies_by_query(self, query: str) -> list:
        """
        Поиск вакансий по ключевому слову
        :param query: поисковой запрос
        :return: список подходящих ваканси
        """
        pass
