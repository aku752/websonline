"""
Django settings for panel_admin project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

#import django_heroku
from pathlib import Path
from .jazzmin import JAZZMIN_SETTINGS
import os

#from django.conf.global_settings import LANGUAGES as DJANGO_LANGUAGES
#from django.utils.translation import gettext_lazy as _
#from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-3bkjqogkktk+zk@-)7(#(tm_utz7f*dkw5g3z5&n!hz8n_w6@j'
SECRET_KEY = 'django-insecure-3bkjqogkktk+zk@-)7(#(tm_utz7f*dkw5g3z5&n!hz8n_w6@j'

# SECURITY WARNING: don't run with debug turned on in production!


# EN ALWAYDATA
DEBUG = True
ALLOWED_HOSTS = ['localhost','*']

# Application definition

INSTALLED_APPS = [   
    'whitenoise.runserver_nostatic',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages', 
    'django.contrib.staticfiles',
    'sitio',
    'servicio',
    'usuario',
    'crispy_forms',
    
]
#CRISPY_TEMPLATE_PACK = 'uni_form'
#CRISPY_TEMPLATE_PACK = 'boostrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #colocar aqui para compatibilidad
   # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'panel_admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #Agregar traductor internacionalizacion
                #'django.template.context_processors.i18n',
                'usuario.context_processors.procesador',                
                #'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'panel_admin.wsgi.application'
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'panel_admin',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
 

# import dj_database_url
# from decouple import config
# DATABASES = {
#     'default': dj_database_url.config(
#         default=config('DATABASE_URL')
#     )
#     }    
# }
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/La_Paz'

USE_I18N = True

USE_L10 = True

USE_TZ = True

#LANGUAGES = DJANGO_LANGUAGES
# LANGUAGES = [
#     ('es', _('Español')),
#     ('en-us', _('English')),
# ]
#LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = 'media/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)    

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#LOGIN_REDIRECT_URL = "/"
# LOGIN_REDIRECT_URL = reverse_lazy('sitio_app:index')
#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
