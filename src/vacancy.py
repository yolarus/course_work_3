class Vacancy:
    """
    Класс для работы с вакансиями
    """
    __slots__ = ("name", "url", "salary", "short_description", "requirements", "area")
    name: str
    url: str
    salary: dict
    short_description: str
    requirements: str
    area: str

    def __init__(self, name: str, url: str, salary: dict, short_description: str, requirements: str, area: str) -> None:
        """
        Конструктор объектов
        """
        self.name = name
        self.url = url
        self.salary = salary
        self.short_description = short_description
        self.requirements = requirements
        self.__check_city(area)

    def __str__(self) -> str:
        return (f"{self.name} -- {self.url}\n"
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
        return {"name": self.name, "url": self.url, "salary": self.salary, "short_description": self.short_description,
                "requirements": self.requirements, "area": self.area}
