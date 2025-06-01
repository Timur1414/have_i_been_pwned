Проект "have i been pwned"
==========================

Этот проект представляет собой реализацию API "have i been pwned" на языке Python с использованием фреймворка Django.
Он позволяет проверять, были ли скомпрометированы учетные данные пользователя в известных утечках данных.
Проект включает в себя функционал для шифрования и дешифрования данных, а также для проверки их на наличие в утечках.

Стек технологий
---------------
- Python
- Django
- Django REST Framework
- Celery
- Redis
- SQLite (или PostgreSQL)
- Docker
- Pycryptodome
- Sphinx
- Pytest
- Pylint
- Алгоритмы шифрования: AES, RSA
- Алгоритмы хеширования: sha256
- Socket

Установка
---------
Создать и активировать виртуальное окружение (версия python = _3.12_).

После этого установить зависимости из файла `requirements.txt`:
```shell
pip install -r requirements.txt
```
Скачать _docker_.

Подготовка
----------
1. Создать файл `.env` в корне проекта и заполнить его на основе `.env.example`:
2. Создать базу данных:
```shell
python manage.py migrate
```
3. Создать суперпользователя:
```shell
python manage.py createsuperuser
````

Запуск
------
1. Запустить Redis:
```shell
docker run -p 6379:6379 redis
```
2. Запустить сервер для шифров:
```shell
python cipher_server.py
```
3. Запустить сервер Django:
```shell
python manage.py runserver
```
4. Запустить Celery (каждую команду в отдельном терминале):
```shell
celery -A have_i_been_pwned beat -l info
celery -A have_i_been_pwned worker -l info --pool=solo
```
