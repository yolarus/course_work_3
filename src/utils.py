from src.vacancy import Vacancy
from src.employer import Employer


def list_of_vacancies(full_info_vacancies: list) -> list[Vacancy]:
    """
    Функция для преобразования списка вакансий из hh.ru в список объектов Vacancy
    :param full_info_vacancies: список вакансий из hh.ru с полной информацией
    :return: список вакансий преобразованных в класс Vacancy
    """
    result = []
    for item in full_info_vacancies:
        result.append(Vacancy(item["name"],
                              item["url"],
                              f'{item["salary"]["from"] if item["salary"]["from"] else item["salary"]["to"]}'
                              f' - {item["salary"]["to"] if item["salary"]["to"] else item["salary"]["from"]}'
                              f' - {item["salary"]["currency"]}',
                              item["snippet"]["responsibility"],
                              item["snippet"]["requirement"],
                              item["area"]["name"]))
    return result


def list_of_employers(full_info_employers: list) -> list[Employer]:
    """
    Функция для преобразования списка работадателей из hh.ru в список объектов Employer
    :param full_info_employers: список работадателей из hh.ru с полной информацией
    :return: список работадателей преобразованных в класс Employer
    """
    result = []
    for item in full_info_employers:
        result.append(Employer(item["name"],
                               item["url"],
                               item["vacancies_url"],
                               item["open_vacancies"]))
    return result


def print_vacancies(vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """
    Функция для вывода в консоль списка объектов класса Vacancy
    :param vacancies: список объектов класса Vacancy
    :param top_n: Максимальное количество вакансий для печати и возврата
    :return: Возращается список объектов класса Vacancy
    """
    flag = 0
    result = []
    for item in vacancies:
        flag += 1
        result.append(item)
        print(item)

        if flag == top_n:
            print("Вывод окончен")
            break
    else:
        print("Вывод окончен")
        if flag == 0:
            print("По вашему запросу не нашлось ни одной вакансии")
        elif flag < top_n:
            print(f"Под ваш запрос подходит лишь {flag} вакансий")
    return result
