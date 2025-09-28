from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost"
]

# Dev-specific CORS
CORS_ALLOW_ALL_ORIGINS = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Development commands
# python3 manage.py runserver --settings=bolnogledachi_bg.settings.dev
# djbolnodev