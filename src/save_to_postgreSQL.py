import os

import psycopg2
from dotenv import load_dotenv
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

load_dotenv(".env")
password_to_postgres = os.getenv("PASSWORD_TO_POSTGRES")


class SaveToDBPostgreSQL:

    @staticmethod
    def create_db(db_name: str) -> None:
        """
        Создание новой БД для последующей работы
        :return: None
        """

        conn = psycopg2.connect(host="localhost",
                                port="5432",
                                user="postgres",
                                password=password_to_postgres,
                                dbname="postgres")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            with conn.cursor() as cur:
                cur.execute(f"DROP DATABASE IF EXISTS {db_name};")
                cur.execute(f"CREATE DATABASE {db_name};")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)
        finally:
            conn.close()

    @staticmethod
    def create_table(table_name: str, headers: list[str]) -> None:
        """
        Создание новой таблицы в БД
        :param table_name: имя таблицы
        :param headers: список строк с именами и типами заголовков таблицы на языке SQL
        :return: None
        """
        conn = psycopg2.connect(host="localhost",
                                port="5432",
                                user="postgres",
                                password=password_to_postgres,
                                dbname="alyautdinov_rt_cw_3")

        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f"DROP TABLE IF EXISTS {table_name}")
                    cur.execute(f"CREATE TABLE {table_name}({', '.join(headers)});")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)
        finally:
            conn.close()

    @staticmethod
    def fill_table(table_name: str, values: list[list]) -> None:
        """
        Заполнение таблицы данным из списка values
        :param table_name: имя таблицы
        :param values: список списков со значениями каждой сущности
        :return: None
        """

        conn = psycopg2.connect(host="localhost",
                                port="5432",
                                user="postgres",
                                password=password_to_postgres,
                                dbname="alyautdinov_rt_cw_3")
        try:
            with conn:
                with conn.cursor() as cur:
                    for value in values:
                        cur.execute(f"INSERT INTO {table_name} VALUES({', '.join(['%s']*len(value))});", value)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)
        finally:
            conn.close()

    @staticmethod
    def add_pk_to_table(table_name: str, column_name: str) -> None:
        """
        Добавление PRIMARY KEY в таблицу
        :param table_name: Имя таблицы для добавления PRIMARY KEY
        :param column_name: Имя столбца, выступающий PRIMARY KEY
        :return: None
        """

        conn = psycopg2.connect(host="localhost",
                                port="5432",
                                user="postgres",
                                password=password_to_postgres,
                                dbname="alyautdinov_rt_cw_3")
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f"ALTER TABLE {table_name} "
                                f"ADD CONSTRAINT pk_{table_name}_{column_name} PRIMARY KEY ({column_name});")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)
        finally:
            conn.close()

    @staticmethod
    def add_fk_to_table(table_name: str, column_name: str, ref_table_name: str, ref_column_name: str) -> None:
        """
        Добавление FOREIGN KEY в таблицу
        :param table_name: Имя таблицы для добавления FOREIGN KEY
        :param column_name: Имя столбца, выступающий FOREIGN KEY
        :param ref_table_name: Имя таблицы, на которую будет ссылаться FOREIGN KEY
        :param ref_column_name: Имя столбца, на который будет ссылаться FOREIGN KEY
        :return: None
        """

        conn = psycopg2.connect(host="localhost",
                                port="5432",
                                user="postgres",
                                password=password_to_postgres,
                                dbname="alyautdinov_rt_cw_3")
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f"ALTER TABLE {table_name} "
                                f"ADD CONSTRAINT fk_{table_name}_{ref_table_name}_{column_name} "
                                f"FOREIGN KEY ({column_name}) REFERENCES {ref_table_name}({ref_column_name});")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)
        finally:
            conn.close()
