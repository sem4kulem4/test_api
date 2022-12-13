# test_api

## Тестовое задание

## Установка

```angular2html
git clone git@github.com:sem4kulem4/test_api.git
python3 -m venv venv
. venv/bin/activate
cd testing/
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

Если нужна админка, то создать суперпользователя:
```angular2html
python3 manage.py createsuperuser
```