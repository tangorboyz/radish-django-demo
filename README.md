# Sample Django Project with Radish-BDD

This is a sample project that using `radish-bdd` with `selenium` to test `django` apps.

## Requirements

- Need RabbitMQ installed for `django-celery-email`
- Python `virtualenv`
- User environment variables: `MAIL_USERNAME` and `MAIL_PASSWORD` for sending email, which used in `mysite/settings/base.py`
- Install all requirements with `pip install -r requirements.txt`

## Run Radish-BDD test

- `RADISH_ONLY=1 python manage.py test`

## DJango Unittest

- `python manage.py test`
