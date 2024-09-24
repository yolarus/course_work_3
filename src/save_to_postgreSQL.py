from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, connection

from src.utils import connect_to_db


class SaveToDBPostgreSQL:
    """
    Класс для создания и заполнения новой базы данных
    """

    @staticmethod
    def __connect_to_db(db_name: str | None = None) -> connection:
        """
        Подключение к БД
        :param db_name: Имя БД
        :return: Объект класса connection
        """
        return connect_to_db(db_name=db_name)

    def create_db(self, db_name: str) -> None:
        """
        Создание новой БД для последующей работы
        :return: None
        """
        try:
            conn = self.__connect_to_db()

            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            with conn.cursor() as cur:
                cur.execute(f"DROP DATABASE IF EXISTS {db_name};")
                cur.execute(f"CREATE DATABASE {db_name};")
            conn.close()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)

    def create_table(self, table_name: str, headers: list[str], db_name: str = "alyautdinov_rt_cw_3") -> None:
        """
        Создание новой таблицы в БД
        :param table_name: имя таблицы
        :param headers: список строк с именами и типами заголовков таблицы на языке SQL
        :param db_name: Имя базы данных
        :return: None
        """

        try:
            conn = self.__connect_to_db(db_name)
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f"DROP TABLE IF EXISTS {table_name}")
                    cur.execute(f"CREATE TABLE {table_name}({', '.join(headers)});")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)

    def fill_table(self, table_name: str, values: list[list], db_name: str = "alyautdinov_rt_cw_3") -> None:
        """
        Заполнение таблицы данным из списка values
        :param table_name: имя таблицы
        :param values: список списков со значениями каждой сущности
        :param db_name: Имя базы данных
        :return: None
        """

        try:
            conn = self.__connect_to_db(db_name)
            with conn:
                with conn.cursor() as cur:
                    for value in values:
                        cur.execute(f"INSERT INTO {table_name} VALUES({', '.join(['%s']*len(value))});", value)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)

    def add_pk_to_table(self, table_name: str, column_name: str, db_name: str = "alyautdinov_rt_cw_3") -> None:
        """
        Добавление PRIMARY KEY в таблицу
        :param table_name: Имя таблицы для добавления PRIMARY KEY
        :param column_name: Имя столбца, выступающий PRIMARY KEY
        :param db_name: Имя базы данных
        :return: None
        """

        try:
            conn = self.__connect_to_db(db_name)
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f"ALTER TABLE {table_name} "
                                f"ADD CONSTRAINT pk_{table_name}_{column_name} PRIMARY KEY ({column_name});")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)

    def add_fk_to_table(self, table_name: str, column_name: str,
                        ref_table_name: str, ref_column_name: str,
                        db_name: str = "alyautdinov_rt_cw_3") -> None:
        """
        Добавление FOREIGN KEY в таблицу
        :param table_name: Имя таблицы для добавления FOREIGN KEY
        :param column_name: Имя столбца, выступающий FOREIGN KEY
        :param ref_table_name: Имя таблицы, на которую будет ссылаться FOREIGN KEY
        :param ref_column_name: Имя столбца, на который будет ссылаться FOREIGN KEY
        :param db_name: Имя базы данных
        :return: None
        """

        try:
            conn = self.__connect_to_db(db_name)
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f"ALTER TABLE {table_name} "
                                f"ADD CONSTRAINT fk_{table_name}_{ref_table_name}_{column_name} "
                                f"FOREIGN KEY ({column_name}) REFERENCES {ref_table_name}({ref_column_name});")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)
