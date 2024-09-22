import os
from typing import Any

import psycopg2
from dotenv import load_dotenv

load_dotenv(".env")
password_to_postgres = os.getenv("PASSWORD_TO_POSTGRES")


def test_save_to_postgresql_create_db(postgre_saver_create_db: Any) -> None:
    """
    Тестирование создания базы данных
    """

    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            user="postgres",
                            password=password_to_postgres)

    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM pg_database WHERE datname = 'alyautdinov_rt_cw_3_test';")
            result = cur.fetchall()[0][0]
    assert result == 1


def test_save_to_postgresql_create_table(postgre_saver_create_db: Any,
                                         postgre_saver_create_table: Any) -> None:
    """
    Тестирование создания таблиц в базе данных
    """

    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            user="postgres",
                            password=password_to_postgres,
                            dbname="alyautdinov_rt_cw_3_test")

    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT EXISTS (SELECT * FROM pg_tables WHERE tablename = 'employers' "
                        "AND schemaname = 'public');")
            result_1 = cur.fetchall()[0][0]
            cur.execute("SELECT EXISTS (SELECT * FROM pg_tables WHERE tablename = 'vacancies' "
                        "AND schemaname = 'public');")
            result_2 = cur.fetchall()[0][0]
    assert result_1 is True
    assert result_2 is True


def test_save_to_postgresql_fill_table(postgre_saver_create_db: Any,
                                       postgre_saver_create_table: Any,
                                       postgre_saver_fill_table: Any) -> None:
    """
    Тестирование заполнения таблиц в базе данных
    """

    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            user="postgres",
                            password=password_to_postgres,
                            dbname="alyautdinov_rt_cw_3_test")

    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT employers.name FROM employers;")
            result = cur.fetchall()
    assert result == [("Test", ), ("Test", )]


def test_save_to_postgresql_add_pk_to_table(postgre_saver_create_db: Any,
                                            postgre_saver_create_table: Any,
                                            postgre_saver_fill_table: Any,
                                            postgre_saver_add_pk: Any) -> None:
    """
    Тестирование добавления PRIMARY KEY в таблицы базы данных
    """

    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            user="postgres",
                            password=password_to_postgres,
                            dbname="alyautdinov_rt_cw_3_test")

    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT C.COLUMN_NAME FROM information_schema.table_constraints "
                        "AS pk INNER JOIN information_schema.KEY_COLUMN_USAGE AS C ON "
                        "C.TABLE_NAME = pk.TABLE_NAME AND "
                        "C.CONSTRAINT_NAME = pk.CONSTRAINT_NAME AND "
                        "C.TABLE_SCHEMA = pk.TABLE_SCHEMA "
                        "WHERE  pk.TABLE_NAME  = 'vacancies' "
                        "AND pk.TABLE_SCHEMA = 'public' "
                        "AND pk.CONSTRAINT_TYPE = 'PRIMARY KEY';")
            result_1 = cur.fetchall()[0][0]
            cur.execute("SELECT C.COLUMN_NAME FROM information_schema.table_constraints "
                        "AS pk INNER JOIN information_schema.KEY_COLUMN_USAGE AS C ON "
                        "C.TABLE_NAME = pk.TABLE_NAME AND "
                        "C.CONSTRAINT_NAME = pk.CONSTRAINT_NAME AND "
                        "C.TABLE_SCHEMA = pk.TABLE_SCHEMA "
                        "WHERE  pk.TABLE_NAME  = 'employers' "
                        "AND pk.TABLE_SCHEMA = 'public' "
                        "AND pk.CONSTRAINT_TYPE = 'PRIMARY KEY';")
            result_2 = cur.fetchall()[0][0]
    assert result_1 == "vacancy_id"
    assert result_2 == "employer_id"


def test_save_to_postgresql_add_fk_to_table(postgre_saver_create_db: Any,
                                            postgre_saver_create_table: Any,
                                            postgre_saver_fill_table: Any,
                                            postgre_saver_add_pk: Any,
                                            postgre_saver_add_fk: Any) -> None:
    """
    Тестирование добавления FOREIGN KEY в таблицу базы данных
    """

    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            user="postgres",
                            password=password_to_postgres,
                            dbname="alyautdinov_rt_cw_3_test")

    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT C.COLUMN_NAME FROM information_schema.table_constraints AS pk "
                        "INNER JOIN information_schema.KEY_COLUMN_USAGE AS C ON "
                        "C.TABLE_NAME = pk.TABLE_NAME AND "
                        "C.CONSTRAINT_NAME = pk.CONSTRAINT_NAME AND "
                        "C.TABLE_SCHEMA = pk.TABLE_SCHEMA "
                        "WHERE  pk.TABLE_NAME  = 'vacancies' "
                        "AND pk.TABLE_SCHEMA = 'public' "
                        "AND pk.CONSTRAINT_TYPE = 'FOREIGN KEY';")
            result = cur.fetchall()[0][0]
    assert result == "employer_id"
