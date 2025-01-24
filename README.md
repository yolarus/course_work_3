# Поиск вакансий на hh.ru c подключением БД

## Описание
Это консольное приложение для поиска вакансий на платформе hh.ru. В приложение встроен следующий функционал:
1. Поиск подходящих работодателей по ключевым словам на hh.ru.
2. Получение списка актуальных вакансий у найденных работодателей.
3. Результаты поиска выгружаются в файлы data/vacancies.json и data/employers.jso, а также сохраняются в новую БД postgreSQL.
4. Выполняется подсчет средней зарплаты по выгруженному списку вакансий, формируется список вакансий с ЗП выше средней. 
5. Фильтрация полученного списка вакансий по ключевым словам в названии вакансии 
6. В проекте настроено тестирование всех классов и функций

## Установка проекта
Клонирование проекта из [GitHub](https://github.com/yolarus/search-for-vacancies-on-hh.ru-with-DB-connection) по HTTPS-токену или SSH-ключу

## Запуск
~ python3 main.py

## Установка зависимостей
1. Перейти в настройки Pycharm -> Setting -> Project -> Python Interpreter 
2. Добавить локальный интерпретатор с менеджером пакетов Poetry
3. Выполнить команду в терминале PyCharm 'poetry install'

## Тестирование
1. Тесты находятся в директории "tests", запуск осуществляется командой
'pytest'. Тесты покрывают 100 % кода. 