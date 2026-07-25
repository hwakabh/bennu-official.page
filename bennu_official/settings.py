import os
import re

from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
DEBUG = False
SECRET_KEY = get_random_secret_key()

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bennuhp',
]

# Strict order for whitenoise
# https://whitenoise.readthedocs.io/en/stable/django.html#enable-whitenoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bennu_official.urls'

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

# adding alias for Vercel deployment
# https://vercel.com/templates/python/django-hello-world
WSGI_APPLICATION = 'bennu_official.wsgi.app'
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.bennu-official.page', '.vercel.app']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Database
DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
    DATABASES = {
        'default': {
            'ENGINE': 'django_libsql',
            'NAME': DATABASE_URL,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': f"{BASE_DIR}/db.sqlite3",
        }
    }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': re.split('[:@/]', os.environ.get('JAWSDB_URL'))[7],
#         'USER': re.split('[:@/]', os.environ.get('JAWSDB_URL'))[3],
#         'PASSWORD': re.split('[:@/]', os.environ.get('JAWSDB_URL'))[4],
#         'HOST': re.split('[:@/]', os.environ.get('JAWSDB_URL'))[5],
#         'PORT': re.split('[:@/]', os.environ.get('JAWSDB_URL'))[6],
#     }
# }

# Password validation
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# - Path of Django will search staticfiles
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)
# - destination path of ./manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# - URL path of staticfiles, which is specified at templates in Pod by buildpacks
STATIC_URL = '/static/'

# Overwrite for local environment
try:
    from .local_settings import *
except ImportError:
    pass
