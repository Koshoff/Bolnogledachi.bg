from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config(
    "DEBUG",
    default=False,
    cast=bool
)

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['bolnogledachi.bg', 'www.bolnogledachi.bg', '46.62.217.246']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Security extras
    'axes',               # brute force protection
    'corsheaders',        # CORS protection
    # 'django_ratelimit',          # rate limiting

    'bolnogledachi_bg.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',   # must be before CommonMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'bolnogledachi_bg.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bolnogledachi_bg.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files configuration
# BASE_DIR = Path(__file__).resolve().parent.parent.parent

# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'  # Where static files are collected
# STATICFILES_DIRS = (
#     BASE_DIR / "static",
# )

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = (
    BASE_DIR / "static",
)

# Media files configuration
MEDIA_URL = '/media/'  # URL to access media files
MEDIA_ROOT = BASE_DIR / 'media'  # Where media files are stored

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AXES_FAILURE_LIMIT = 5  # колко неуспешни login опита да блокира
AXES_COOLOFF_TIME = 1   # час(ове), колко време да е блокирано

# Email settings (Purelymail)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.purelymail.com'
EMAIL_PORT = 587             # TLS порт
EMAIL_USE_TLS = True         # използвай TLS (STARTTLS)
EMAIL_USE_SSL = False        # не ползвай SSL
EMAIL_HOST_USER = 'contact@bolnogledachi.bg'
EMAIL_HOST_PASSWORD = 'Yotovconsulting9761bolnogledachi' 
DEFAULT_FROM_EMAIL = 'Болногледачи.бг <contact@bolnogledachi.bg>'
CONTACT_RECEIVER_EMAIL = 'contact@bolnogledachi.bg'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = True         # използвай TLS (STARTTLS)
EMAIL_USE_SSL = False        # не ползвай SSL
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
CONTACT_RECEIVER_EMAIL = config('CONTACT_RECEIVER_EMAIL')