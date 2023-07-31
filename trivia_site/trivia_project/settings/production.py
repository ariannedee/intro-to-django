from .base import *

ALLOWED_HOSTS = ['trivia-ariannedee.pythonanywhere.com']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ariannedee$trivia",
        "USER": "ariannedee",
        "PASSWORD": env("DB_PASSWORD", None),
        "HOST": "ariannedee.mysql.pythonanywhere-services.com",
        "ATOMIC_REQUESTS": True,
        "CONN_MAX_AGE": env.int("CONN_MAX_AGE", default=60),
    }
}

# Email for user registration and password reset
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL_ADDRESS", "")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD", "")
