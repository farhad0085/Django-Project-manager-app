import os

DEBUG = False
ALLOWED_HOSTS = ['*']

WEBSITE_BASE_URL = "http://localhost:3000" # react frontend
WEBSITE_BACKEND_URL = "http://localhost:8000"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DBNAME'),
        'USER': os.getenv('DBUSER'),
        'PASSWORD': os.getenv('DBPASS'),
        'HOST': os.getenv('DBHOST'),
        'PORT': os.getenv('DBPORT')
    }
}