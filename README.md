# Дипломный проект курса "Инженер по тестированию: от новичка до автоматизатора"
## Задания по теме "API-тестирование"

    API-тесты на сервис Stellar Burgers. 
    Это космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.

## Файлы
    - tests/  -  каталог с тестами
    - tests/conftest.py  -  файл с фикстурами
    - data.py  -  файл с постоянными использукемыми в проверках
    - help.py  -  вспомогательные методы используемые в проверках


## Команды

Запустить тесты

    pytest tests --alluredir=allure_results

Посмотреть веб отчет

    allure serve allure_results

Посмотреть степень покрытия

    pytest --cov  