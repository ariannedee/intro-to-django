from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
SECRET_KEY = 'django-insecure-xk@mwgnc4bjx&xvass@y3*cu@v2uw+++uzh*@knxnp8j^8#jyh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Needed for Django Debug Toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/
INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    "127.0.0.1",
]