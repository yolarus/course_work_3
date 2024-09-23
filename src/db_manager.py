from psycopg2 import Error
from psycopg2.extensions import connection

from src.utils import connect_to_db


class DBManager:
    """
    Класс для работы с БД
    """

    @staticmethod
    def __connect_to_db(db_name: str | None = None) -> connection:
        """
        Подключение к БД
        :param db_name: Имя БД
        :return: Объект класса connection
        """
        return connect_to_db(db_name=db_name)

    def get_companies_and_vacancies_count(self, db_name: str = "alyautdinov_rt_cw_3") -> list:
        """
        Получение списка всех компаний и количества вакансий у каждой компании
        :param db_name: Имя базы данных
        :return: Список кортежей: компания - количество вакансий
        """

        conn = self.__connect_to_db(db_name)

        result = []
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT name, open_vacancies FROM employers")
                    result = cur.fetchall()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)

        return result

    def get_all_vacancies(self, db_name: str = "alyautdinov_rt_cw_3") -> list:
        """
        Получение списка всех вакансий
        :param db_name: Имя базы данных
        :return: Список кортежей: название компании - название вакансии - зарплата от - зарплата до
         - зарплата валюта - ссылка на вакансию
        """

        conn = self.__connect_to_db(db_name)

        result = []
        try:
            with conn:
                with conn.cursor() as cur:
                    query = ("SELECT employers.name, vacancies.name, vacancies.salary_from, "
                             "vacancies.salary_to, vacancies.salary_currency, vacancies.url FROM employers "
                             "JOIN vacancies USING (employer_id);")
                    cur.execute(query)
                    result = cur.fetchall()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)

        return result

    def get_avg_salary(self, currency: str = "RUR", db_name: str = "alyautdinov_rt_cw_3") -> str:
        """
        Получение средней зарплаты по вакансиям в заданной валюте
        :param currency: Код валюты в формате 'RUR'
        :param db_name: Имя базы данных
        :return: Средняя зарплата по вакансиям
        """

        conn = self.__connect_to_db(db_name)

        result = ""
        try:
            with conn:
                with conn.cursor() as cur:
                    query = (f"SELECT AVG(salary_from), AVG(salary_to) FROM vacancies "
                             f"WHERE salary_currency = '{currency}';")
                    cur.execute(query)
                    res = cur.fetchall()
                    result = f"{round(sum(res[0]) / len(res[0]), 2)} {currency}"
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)

        return result

    def get_vacancies_with_higher_salary(self, currency: str = "RUR", db_name: str = "alyautdinov_rt_cw_3") -> list:
        """
        Получение списка вакансий с зарплатой выше среднего
        :param currency: Код валюты в формате 'RUR'
        :param db_name: Имя базы данных
        :return: Список кортежей: название компании - название вакансии - зарплата от - зарплата до
         - зарплата валюта - ссылка на вакансию
        """

        avg_salary = float(self.get_avg_salary(currency, db_name).split()[0])

        conn = self.__connect_to_db(db_name)

        result = []
        try:
            with conn:
                with conn.cursor() as cur:
                    query = (f"SELECT employers.name, vacancies.name, vacancies.salary_from, "
                             f"vacancies.salary_to, vacancies.salary_currency, vacancies.url FROM employers "
                             f"JOIN vacancies USING (employer_id)"
                             f"WHERE vacancies.salary_from > {avg_salary} "
                             f"AND vacancies.salary_currency = '{currency}';")
                    cur.execute(query)
                    result = cur.fetchall()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)

        return result

    def get_vacancies_with_keyword(self, keyword: str, db_name: str = "alyautdinov_rt_cw_3") -> list:
        """
        Получение списка вакансий по ключевому слову в названии
        :param db_name: Имя базы данных
        :param keyword: Ключевое слово для поиска
        :return: Список кортежей: название компании - название вакансии - зарплата от - зарплата до
         - зарплата валюта - ссылка на вакансию
        """

        conn = self.__connect_to_db(db_name)

        result = []

        try:
            with conn:
                with conn.cursor() as cur:
                    query = (f"SELECT employers.name, vacancies.name, vacancies.salary_from, "
                             f"vacancies.salary_to, vacancies.salary_currency, vacancies.url FROM employers "
                             f"JOIN vacancies USING (employer_id)"
                             f"WHERE vacancies.name LIKE '%{keyword}%' OR vacancies.name LIKE '%{keyword.lower()}%';")
                    cur.execute(query)
                    result = cur.fetchall()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)

        return result
