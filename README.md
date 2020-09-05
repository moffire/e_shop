# e_shop

Интернет магазин с возможностью оплаты банковской картой и системой купонов

# Установка

## Клонировать репозиторий:
* git clone git@github.com:moffire/e_shop.git
* cd e_shop
## Создать виртуальное окружение и установить зависимости:
* virtualenv --no-site-packages env
* source env/bin/activate
* pip install -r requirements.txt
* **Ввести данные аккаунта Braintree в settings.py для оплаты картой**
* ./manage.py makemigrations
* ./manage.py migrate

## Использованные технологии

* Django 3.1
* PostgreSQL
* Redis
* Celery
* RabbitMQ
* Braintree API
