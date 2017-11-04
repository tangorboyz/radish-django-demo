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