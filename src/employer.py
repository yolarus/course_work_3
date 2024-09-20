class Employer:
    """
    Класс для работы с работодателями
    """
    __slots__ = ("employer_id", "name", "url", "url_to_vacancies_list", "open_vacancies")
    ID: int = 0
    employer_id: int
    name: str
    url: str
    url_to_vacancies_list: str
    open_vacancies: int

    def __init__(self, name: str, url: str, url_to_vacancies_list: str, open_vacancies: int) -> None:
        """
        Конструктор объектов
        """
        Employer.ID += 1
        self.employer_id = Employer.ID
        self.name = name
        self.url = url
        self.url_to_vacancies_list = url_to_vacancies_list
        self.open_vacancies = open_vacancies

    def __str__(self) -> str:
        return (f"ID: {self.employer_id} -- {self.name} -- {self.url}\n"
                f"Доступные вакансии: {self.url_to_vacancies_list}\n"
                f"Всего открытых вакансий: {self.open_vacancies}\n")
