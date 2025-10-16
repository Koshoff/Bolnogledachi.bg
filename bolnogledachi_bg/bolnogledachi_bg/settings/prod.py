from .base import *

DEBUG = False

ALLOWED_HOSTS = ['46.62.217.246', 'bolnogledachi.bg', 'www.bolnogledachi.bg', 'localhost', '127.0.0.1']
# ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")])

# Security settings for production
# # SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# X_FRAME_OPTIONS = "DENY"
# SECURE_CONTENT_TYPE_NOSNIFF = True

# # HTTP Strict Transport Security (HSTS)
# SECURE_HSTS_SECONDS = 31536000  # 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# Brute force protection settings
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'axes.backends.AxesStandaloneBackend',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

# Production commands
# python3 manage.py runserver --settings=bolnogledachi_bg.settings.prod
# djbolnoprod
# bolno_deploy