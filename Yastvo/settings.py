"""
Django settings for Yastvo project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os.path
from pathlib import Path
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t)wg^gec38yvjwcriylwc=!i8x*ms3qag02y1%je2_#+*!$%!a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'modeltranslation', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'django.contrib.sites',
    'main',
    'delivery',
    'rosetta',
   
        ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Yastvo.urls'

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

WSGI_APPLICATION = 'Yastvo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '37485482_yastvo',
#         'USER': 'DemetrPI',
#         'PASSWORD': 'oYP9irX8YwqsQXWU',
#         'HOST': 'serwer2329268.home.pl',
#         'PORT': '3306', # or the port provided by your hosting provider
#     }
# }

DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'Yastvo',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host' : "mongodb+srv://DemetrPI:3PzaX7E1PrgwF5kz@yastvo.qruoho3.mongodb.net/?retryWrites=true&w=majority"
            }  
        }
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGE_COOKIE_NAME = 'django_language'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', _('English')),
    ('uk', _('Ukrainian')),
    ('pl',_('Polish'))
)

LOCALE_PATHS = (os.path.join(BASE_DIR,'locale/'),)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'staticfiles')
#  ]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    
)

MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR,'images')

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'users'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1

#stripe payment
STRIPE_KEY = ''

TRANSLATABLE_MODEL_MODULES = [
    "menuItems",
]



# This can be a string or callable, and should return a base host that
# will be used when receiving callbacks and notifications from payment
# providers.
#
# Keep in mind that if you use `localhost`, external servers won't be
# able to reach you for webhook notifications.
PAYMENT_HOST = 'localhost:8000'

# Whether to use TLS (HTTPS). If false, will use plain-text HTTP.
# Defaults to ``not settings.DEBUG``.
PAYMENT_USES_SSL = False