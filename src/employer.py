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

    def to_dict(self) -> dict:
        """
        Конвертация объекта класса Employer в словарь
        """
        return {"employer_id": self.employer_id,
                "name": self.name,
                "url": self.url,
                "url_to_vacancies_list": self.url_to_vacancies_list,
                "open_vacancies": self.open_vacancies}

    @staticmethod
    def get_headers_to_db() -> list:
        """
        Получение заголовков столбцов для загрузки данных в БД
        :return: Список строк с именами и типами данных заголовков на языке SQL
        """
        return ["employer_id int",
                "name varchar(255)",
                "url varchar(255)",
                "url_to_vacancies_list varchar(255)",
                "open_vacancies int"]

    def get_insert_data_to_db(self) -> list:
        """
        Получение данных для заполнения таблиц в БД
        :return: Список атрибутов экземпляра
        """
        return [self.employer_id,
                self.name,
                self.url,
                self.url_to_vacancies_list,
                self.open_vacancies]
