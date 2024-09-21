import os
from dotenv import load_dotenv
from src.save_to_postgreSQL import SaveToDBPostgreSQL
import psycopg2
from typing import Any
from unittest.mock import patch

load_dotenv(".env")
password_to_postgres = os.getenv("PASSWORD_TO_POSTGRES")


def test_save_to_postgresql_create_db(postgre_saver: SaveToDBPostgreSQL) -> None:
    """
    Тестирование создания базы данных
    """
    postgre_saver.create_db("alyautdinov_rt_cw_3_test")

    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            user="postgres",
                            password=password_to_postgres,
                            dbname="alyautdinov_rt_cw_3_test")

    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM pg_database WHERE datname = 'alyautdinov_rt_cw_3_test';")
            result = cur.fetchall()[0][0]
    assert result == 1


def test_save_to_postgresql_create_table(postgre_saver: SaveToDBPostgreSQL) -> None:
    """
    Тестирование создания таблицы в базе данных
    """
    postgre_saver.create_table("test_1",
                               ["test_id int", "test varchar(4)"],
                               "alyautdinov_rt_cw_3_test")

    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            user="postgres",
                            password=password_to_postgres,
                            dbname="alyautdinov_rt_cw_3_test")

    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT EXISTS (SELECT * FROM pg_tables WHERE tablename = 'test_1' AND schemaname = 'public');")
            result = cur.fetchall()[0][0]
    assert result is True


def test_save_to_postgresql_fill_table(postgre_saver: SaveToDBPostgreSQL) -> None:
    """
    Тестирование создания таблицы в базе данных
    """
    postgre_saver.fill_table("test_1",
                             [[1, "1111"], [2, "2222"]],
                             "alyautdinov_rt_cw_3_test")

    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            user="postgres",
                            password=password_to_postgres,
                            dbname="alyautdinov_rt_cw_3_test")

    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM test_1;")
            result = cur.fetchall()
    assert result == [(1, "1111"), (2, "2222")]


def test_save_to_postgresql_add_pk_to_table(postgre_saver: SaveToDBPostgreSQL) -> None:
    """
    Тестирование добавления PRIMARY KEY в таблицу базы данных
    """
    postgre_saver.add_pk_to_table("test_1",
                                  "test_id",
                                  "alyautdinov_rt_cw_3_test")

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
                        "WHERE  pk.TABLE_NAME  = 'test_1' "
                        "AND pk.TABLE_SCHEMA = 'public' "
                        "AND pk.CONSTRAINT_TYPE = 'PRIMARY KEY';")
            result = cur.fetchall()[0][0]
    assert result == "test_id"


def test_save_to_postgresql_add_fk_to_table(postgre_saver: SaveToDBPostgreSQL) -> None:
    """
    Тестирование добавления FOREIGN KEY в таблицу базы данных
    """
    postgre_saver.create_table("check_1",
                               ["check_id int", "test_id int", "test varchar(6)"],
                               "alyautdinov_rt_cw_3_test")

    postgre_saver.fill_table("check_1",
                             [[1, 1, "111111"], [2, 1, "222222"], [3, 2, "333333"], [4, 2, "444444"]],
                             "alyautdinov_rt_cw_3_test")

    postgre_saver.add_fk_to_table("check_1",
                                  "test_id",
                                  "test_1",
                                  "test_id",
                                  "alyautdinov_rt_cw_3_test")

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
                        "WHERE  pk.TABLE_NAME  = 'check_1' "
                        "AND pk.TABLE_SCHEMA = 'public' "
                        "AND pk.CONSTRAINT_TYPE = 'FOREIGN KEY';")
            result = cur.fetchall()[0][0]
    assert result == "test_id"
