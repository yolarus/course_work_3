import os
from typing import Optional

import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import connection

from src.employer import Employer
from src.save_to_json_file import SaveToJSONFile
from src.vacancy import Vacancy

load_dotenv(".env")
host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER_NAME")
password_to_postgres = os.getenv("PASSWORD_TO_POSTGRES")


def list_of_vacancies(full_info_vacancies: list, employer_id: Optional[int] = None) -> list[Vacancy]:
    """
    Функция для преобразования списка вакансий из hh.ru в список объектов Vacancy
    :param full_info_vacancies: список вакансий из hh.ru с полной информацией
    :param employer_id: опциональный параметр для присвоения локального id работодателя
    :return: список вакансий преобразованных в класс Vacancy
    """
    result = []
    for item in full_info_vacancies:
        new_vacancy = Vacancy(item["name"],
                              item["url"],
                              {"from": int(item["salary"]["from"])
                              if item["salary"]["from"]
                              else item["salary"]["to"],
                               "to": int(item["salary"]["to"])
                               if item["salary"]["to"]
                               else int(item["salary"]["from"]),
                               "currency": item["salary"]["currency"]},
                              item["snippet"]["responsibility"],
                              item["snippet"]["requirement"],
                              item["area"]["name"])
        if employer_id:
            new_vacancy.employer_id = employer_id
        result.append(new_vacancy)
    return result


def list_of_employers(full_info_employers: list) -> list[Employer]:
    """
    Функция для преобразования списка работодателей из hh.ru в список объектов Employer
    :param full_info_employers: список работодателей из hh.ru с полной информацией
    :return: список работодателей преобразованных в класс Employer
    """
    result = []
    for item in full_info_employers:
        result.append(Employer(item["name"],
                               item["url"],
                               item["vacancies_url"],
                               item["open_vacancies"] if item["open_vacancies"] <= 20 else 20))
    return result


def use_to_list_json_saver(items: list, file_name: str) -> None:
    """
    Функция для быстрого сохранения через класс SaveToJSONFile списка объектов
    :param items: Список объектов для сохранения
    :param file_name: Имя файла для сохранения данных
    :return: None
    """

    item_json_saver = SaveToJSONFile(file_name)
    item_json_saver.clear_file()
    for item in items:
        item_json_saver.add_to_file(item)
    print(f"Данные выгружены в файл: data/{file_name}.json")


def connect_to_db(host: str | None = host,
                  port: str | None = port,
                  user: str | None = user,
                  password: str | None = password_to_postgres,
                  db_name: str | None = None) -> connection:
    """
    Функция для подключения к БД postgreSQL
    :param host: Имя сервера
    :param port: Номер порта
    :param user: Имя пользователя
    :param password: Пароль пользователя
    :param db_name: Имя БД
    :return: Объект connection
    """
    return psycopg2.connect(host=host,
                            port=port,
                            user=user,
                            password=password,
                            dbname=db_name)
