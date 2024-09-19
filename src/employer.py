class Employer:
    """
    Класс для работы с работодателями
    """
    __slots__ = ("name", "url", "url_to_vacancies_list", "open_vacancies")
    name: str
    url: str
    url_to_vacancies_list: str
    open_vacancies: int

    def __init__(self, name: str, url: str, url_to_vacancies_list: str, open_vacancies: int) -> None:
        """
        Конструктор объектов
        """
        self.name = name
        self.url = url
        self.url_to_vacancies_list = url_to_vacancies_list
        self.open_vacancies = open_vacancies

    def __str__(self) -> str:
        return (f"{self.name} -- {self.url} -- Доступные вакансии: {self.url_to_vacancies_list}\n"
                f" -- Всего открытых вакансий: {self.open_vacancies}\n")
