from typing import Optional


class Vacancy:
    """
    Класс для работы с вакансиями
    """
    __slots__ = ("vacancy_id", "employer_id", "name", "url", "salary", "short_description", "requirements", "area")
    ID: int = 0
    vacancy_id: int
    employer_id: Optional[int]
    name: str
    url: str
    salary: dict
    short_description: str
    requirements: str
    area: str

    def __init__(self, name: str, url: str, salary: dict,
                 short_description: str, requirements: str, area: str, employer_id: Optional[int] = None) -> None:
        """
        Конструктор объектов
        """
        Vacancy.ID += 1
        self.vacancy_id = Vacancy.ID
        self.name = name
        self.url = url
        self.salary = salary
        self.short_description = short_description
        self.requirements = requirements
        self.__check_city(area)
        self.employer_id = employer_id

    def __str__(self) -> str:
        return (f"ID: {self.vacancy_id} -- ID работодателя: {self.employer_id} -- {self.name} -- {self.url}\n"
                f"Зарплата: от {self.salary['from']} до {self.salary['to']} {self.salary['currency']}\n"
                f"Краткое описание: {self.short_description}\n"
                f"Требования: {self.requirements}\n"
                f"Место работы: {self.area}\n")

    def __eq__(self, other: "Vacancy") -> bool:   # type: ignore[override]
        """
        Метод для проверки зарплат вакансий - равно
        """
        if (self.salary["from"] == other.salary["from"]
                and self.salary["currency"] == other.salary["currency"]):
            return True
        else:
            return False

    def __lt__(self, other: "Vacancy") -> bool:
        """
        Метод для проверки зарплат вакансий - меньше
        """
        if (self.salary["from"] < other.salary["from"]
                and self.salary["currency"] == other.salary["currency"]):
            return True
        else:
            return False

    def __le__(self, other: "Vacancy") -> bool:
        """
        Метод для проверки зарплат вакансий - меньше или равно
        """
        if (int(self.salary["from"]) <= int(other.salary["from"])
                and self.salary["currency"] == other.salary["currency"]):
            return True
        else:
            return False

    def __check_city(self, area: str) -> None:
        """
        Валидация вакансии по месту работы
        :param area: Место работы
        :return: None
        """
        if area == "Москва":
            self.area = area
        else:
            self.area = "Можно не рассматривать данную вакансию"

    def to_dict(self) -> dict:
        """
        Конвертация объекта класса Vacancy в словарь
        """
        return {"vacancy_id": self.vacancy_id, "employer_id": self.employer_id, "name": self.name,
                "url": self.url, "salary": self.salary, "short_description": self.short_description,
                "requirements": self.requirements, "area": self.area}

    @staticmethod
    def get_headers_to_db() -> list:
        """
        Получение заголовков столбцов для загрузки данных в БД
        :return: Список строк с именами и типами данных заголовков на языке SQL
        """
        return ["vacancy_id int",
                "employer_id int",
                "name varchar(255)",
                "url varchar(255)",
                "salary_from int",
                "salary_to int",
                "salary_currency varchar(3)",
                "short_description text",
                "requirements text",
                "area varchar(255)"]

    def get_insert_data_to_db(self) -> list:
        """
        Получение данных для заполнения таблиц в БД
        :return: Список атрибутов экземпляра
        """
        return [self.vacancy_id,
                self.employer_id,
                self.name,
                self.url,
                self.salary["from"],
                self.salary["to"],
                self.salary["currency"],
                self.short_description,
                self.requirements,
                self.area]
