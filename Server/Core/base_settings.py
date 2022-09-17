"""
Django settings for Core project.

from django.contrib.sites.models import Site
new_site = Site.objects.create(domain='foo.com', name='foo.com')
print new_site.id

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
import socket
from datetime import timedelta

from django.conf import settings


# Build paths inside the project like this: os.path.join(BASE_DIR,
# Preferances
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(BASE_DIR, '../')


# Quick-start development settings - unsuitable for production
# See
# https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY', 'not-so-secret-key')
SECRET_KEY = '5%5e%41(8ps!r36)r=i(ismmdcf0%@*zmchhg*4-5_i-0cbryf'


# SECURITY WARNING: don't run with debug turned on in production!
# Hosts
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of
    # `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Application definition

AUTHENTICATION_REST_APPS = [
    'django.contrib.sites',
    'django.contrib.auth',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'django_rest_passwordreset',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',

]


CUSTOM_APPS = [

]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'multiselectfield',
    'django_seed',

]

# Adding Django Apps

INSTALLED_APPS += AUTHENTICATION_REST_APPS
INSTALLED_APPS += CUSTOM_APPS
CELERY_RESULT_BACKEND = "django-db"
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
TEMPLATE_CONTEXT_PROCESSORS = (
    ...,
    # 'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
    "module.context_processors.site",
    ...
)
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware'
]

ROOT_URLCONF = 'Core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'Core/', 'templates')
                 ],
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

WSGI_APPLICATION = 'Core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases adventurebookings_db


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + '/db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 4,
        }
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    # 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'en-uk'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Africa/Harare'
USE_I18N = False

USE_L10N = True
# USE_L10N = False
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'



STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'static_root')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

