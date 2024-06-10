import os
from .base import BASE_DIR

DEBUG = True

ALLOWED_HOSTS = ['*']

WEBSITE_BASE_URL = "http://localhost:3000" # react frontend
WEBSITE_BACKEND_URL = "http://localhost:8000"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
