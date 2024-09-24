import json

from src.save_to_json_file import SaveToJSONFile
from src.vacancy import Vacancy


def test_save_to_json_save_to_file(saver_json: SaveToJSONFile,
                                   first_vacancy: Vacancy,
                                   first_vacancy_dict: dict) -> None:
    """
    Тест сохранения в новый файл .json / перезаписи файла .json
    """
    saver_json.save_to_file(first_vacancy)

    with open("data/test_data/test.json", "r", encoding="UTF-8") as f:
        data = json.load(f)
    assert data == [first_vacancy_dict]


def test_save_to_json_read_from_file(saver_json: SaveToJSONFile,
                                     first_vacancy_dict: dict) -> None:
    """
    Тест чтения из файла .json
    """
    saver_json.read_from_file()
    with open("data/test_data/test.json", "r", encoding="UTF-8") as f:
        data = json.load(f)
    assert data == [first_vacancy_dict]


def test_save_to_json_add_to_file(saver_json: SaveToJSONFile,
                                  first_vacancy: Vacancy,
                                  second_vacancy: Vacancy,
                                  first_vacancy_dict: dict,
                                  second_vacancy_dict: dict) -> None:
    """
    Тест добавления в файл .json
    """
    saver_json.add_to_file(second_vacancy)
    with open("data/test_data/test.json", "r", encoding="UTF-8") as f:
        data = json.load(f)
    assert data == [first_vacancy_dict, second_vacancy_dict]


def test_save_to_json_add_to_file_dupl(saver_json: SaveToJSONFile,
                                       first_vacancy: Vacancy,
                                       second_vacancy: Vacancy,
                                       first_vacancy_dict: dict,
                                       second_vacancy_dict: dict) -> None:
    """
    Тест добавления дубликата в файл .json
    """
    saver_json.add_to_file(second_vacancy)
    with open("data/test_data/test.json", "r", encoding="UTF-8") as f:
        data = json.load(f)
    assert data == [first_vacancy_dict, second_vacancy_dict]


def test_save_to_json_delete_from_file(saver_json: SaveToJSONFile,
                                       first_vacancy: Vacancy,
                                       second_vacancy: Vacancy,
                                       first_vacancy_dict: dict) -> None:
    """
    Тест удаления вакансии из файла .json
    """
    saver_json.delete_from_file(second_vacancy)
    with open("data/test_data/test.json", "r", encoding="UTF-8") as f:
        data = json.load(f)
    assert data == [first_vacancy_dict]


def test_save_to_json_clear_file(saver_json: SaveToJSONFile) -> None:
    """
    Тест очистки файла .json
    """
    saver_json.clear_file()
    with open("data/test_data/test.json", "r", encoding="UTF-8") as f:
        data = json.load(f)
    assert data == []
