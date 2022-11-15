import os
import local_settings

from datetime import timedelta
from pathlib import Path

from .logger import DjangoColorsFormatter

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================================
# APPS SETTINGS
# ==============================================================================

SECRET_KEY = os.environ.get("SECRET_KEY", default='django-insecure-v6$@j@0-xcje+wg-)g*!0dm!tfdghf^&%3dfg%+f&5nn^fi0')

DEBUG = int(os.environ.get("DEBUG", default=1))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default='localhost 127.0.0.1 [::1]').split(" ")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',

    'corsheaders',
    'rest_framework',
    'drf_yasg',
    'django_celery_beat',

    'apps.core.apps.CoreConfig',
    'apps.api.apps.ApiConfig',
    'apps.tasks.apps.TasksConfig',
    'apps.telebot.apps.TelebotConfig',
]

# ==============================================================================
# DRF SETTINGS
# ==============================================================================

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# ==============================================================================
# JWT SETTINGS
# ==============================================================================

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.admindocs.middleware.XViewMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

# ==============================================================================
# DATABASE SETTINGS
# ==============================================================================

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

# ==============================================================================
# VALIDATORS SETTINGS
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ==============================================================================
# MORE SETTINGS
# ==============================================================================

AUTH_USER_MODEL = 'core.User'

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True

# ==============================================================================
# CELERY SETTINGS
# ==============================================================================

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER", "redis://redis:6379/0")
CELERYD_HIJACK_ROOT_LOGGER = False

CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# ==============================================================================
# TELEGRAM LOGGER SETTINGS
# ==============================================================================

TELEGRAM_LOGGING_TOKEN = os.environ.get("TELEGRAM_TOKEN", local_settings.TELEGRAM_TOKEN)
TELEGRAM_LOGGING_CHAT = os.environ.get("TELEGRAM_GROUP_ID", local_settings.TELEGRAM_GROUP_ID)
TELEGRAM_LOGGING_EMIT_ON_DEBUG = True

# ==============================================================================
# TELEGRAM LOGGER SETTINGS
# ==============================================================================

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", local_settings.TELEGRAM_BOT_TOKEN)

# ==============================================================================
# LOGGER SETTINGS
# ==============================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s %(levelname)s %(name)s - %(message)s]',
            'datefmt': '%Y.%m.%d %H:%M:%S',
        },
        'colored': {
            '()': DjangoColorsFormatter,
            'format': '[%(asctime)s] - %(levelname)s - %(message)s \n',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
        'default': {
            'format': '[{levelname}]-[{asctime}]-[{module}]-[{process:d}]-[{thread:d}]: {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'handlers': {
        'console_prod': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['require_debug_false'],
            'level': 'ERROR',
        },
        'console_debug': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['require_debug_true'],
            'level': 'DEBUG',
        },
        'backend_log': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/backend.log',
            'level': 'INFO',
            'formatter': 'simple',
        },
        'critical_error_log': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/backend_errors.log',
            'level': 'ERROR',
            'formatter': 'simple',
        },
        'celery_log': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/celery_worker.log',
            'level': 'INFO',
            'formatter': 'default',
        },
        'telegram_log': {
            'level': 'ERROR',
            'class': 'apps.telebot.handler.TelegramHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console_debug', 'backend_log', 'telegram_log', 'critical_error_log'],
            'propagate': False,
        },
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['console_debug', 'backend_log', 'telegram_log', 'critical_error_log'],
            'propagate': False,
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console_debug', 'backend_log', 'telegram_log', 'critical_error_log'],
            'propagate': False,
        },
        'celery': {
            'level': 'DEBUG',
            'handlers': ['console_debug', 'celery_log', 'telegram_log', 'critical_error_log']
        },
    },
}

# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_HOST = os.environ.get("EMAIL_HOST", local_settings.EMAIL_HOST)
EMAIL_PORT = os.environ.get("EMAIL_PORT", local_settings.EMAIL_PORT)
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", local_settings.EMAIL_HOST_USER)
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", local_settings.EMAIL_HOST_PASSWORD)
# EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", local_settings.EMAIL_USE_TLS)
EMAIL_USE_SSL = os.environ.get("EMAIL_USE_SSL", local_settings.EMAIL_USE_SSL)
