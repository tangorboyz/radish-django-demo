# Sample Django Project with Radish-BDD

This is a sample project that using `radish-bdd` with `selenium` to test `django` apps.

## Requirements

- Need RabbitMQ installed for `django-celery-email`
- Python `virtualenv`
- User environment variables: `MAIL_USERNAME` and `MAIL_PASSWORD` for sending email, which used in `mysite/settings/base.py`
- Install all requirements with `pip install -r requirements.txt`

## Run Project

- Install RabbitMQ-server
- After setting environment variable for `MAIL_USERNAME` and `MAIL_PASSWORD`, go to project root folder and active at least three python   `virtualenv`. First for `celery`, second for `django` development server, third for `radish-bdd`.
- export the path to feature testing with `export DJANGO_SETTINGS_MODULE=mysite.settings.feature` on each of that running virtualenv.
- Run `celery` with `celery -E -A mysite worker -l info`
- Run django development server with `python manage.py runserver`
- Run `radish` with  `PYTHONPATH=. radish features/`

## Summary

It would seem that the problem caused by timezone settings in Django settings file, which is default to `UTC`, while my timezone is `UTC+8`. But in my opinion, that `radish` timer shouldn't depend on timezone settings.

Even python timedelta also failed to count the time.

I have created 5 branch to show the difference between timezone settings.

## Note

This just a soulution, when I want to use radish with selenium. I really like the gherkin style. It makes our requirements clear. However, I've encounter a few problem:

- I need that the database will be cleaned up after every scenario, to avoid headache to remember which data is belong to. DJango use two database name, one on its default with `some_db_name` for development and a second with `test_some_db_name` which is used on unittest. Becase I used django LiveTestCase to automatically reset the database, Database that being used with radish is different from the database on running server. So I adjust the database settings like this:

```
# mysite.settings.feature
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_features',
        'HOST': 'localhost',
        'PORT': '',
        'USER': 'goat',
        'PASSWORD': '',
        'TEST': {
            'NAME': 'blog_features'
        }
    },
}

# mysite.settings.base
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'HOST': 'localhost',
        'PORT': '',
        'USER': 'goat',
        'PASSWORD': '',
    },
}

```

I created two setting files, one for unittest and another for radish. By setting test database name same to the default name, I allow radish use the same database on running server. But that's okay on mysql or sqlite. PostgreSQL will reject connection, If we are gonna drop database while it still being used on its session.
So I dropped a question on stackoverflow, to look for an answer about the cause. I didn't know that PotgreSQL have that rules. And for that, I got -1 for using a stupid solution. But that's okay, as long as I got the answer that I was looking for. "Too shy (pride) to ask and you will lost on your way". I also got another -1 for asking for a solution about reset the database on each scenario, as I post my own solution that super slow in terms of speed of test.
But all of them give an answer. And there's a solution about integrating radish with django command. So we could run it with `python manage.py test`. I haven't try it yet.