"""
Django settings for notices-api project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')v(s0wbqw24q--b05=fy=$5pte2zqzihctbp(+lwy8rff)r8qw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.43.215', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'rest_framework.authtoken',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'testapi.urls'

#tell django we created custom user account
AUTH_USER_MODEL = 'accounts.Account'

#Restframework permissions
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        ),
    'EXCEPTION_HANDLER': 'accounts.utils.custom_exception_handler'
}


# Default JWT preferences
JWT_AUTH = {
'JWT_ENCODE_HANDLER':
'rest_framework_jwt.utils.jwt_encode_handler',
'JWT_DECODE_HANDLER':
'rest_framework_jwt.utils.jwt_decode_handler',
'JWT_PAYLOAD_HANDLER':
'rest_framework_jwt.utils.jwt_payload_handler',
'JWT_PAYLOAD_GET_USER_ID_HANDLER':
'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
'JWT_RESPONSE_PAYLOAD_HANDLER':
'rest_framework_jwt.utils.jwt_response_payload_handler',
'JWT_SECRET_KEY': SECRET_KEY,
'JWT_ALGORITHM': 'HS256',
'JWT_VERIFY': True,
'JWT_VERIFY_EXPIRATION': True,
'JWT_LEEWAY': 0,
'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
'JWT_AUDIENCE': None,
'JWT_ISSUER': None,
'JWT_ALLOW_REFRESH': False,
'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
'JWT_AUTH_HEADER_PREFIX': 'JWT',
}



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

WSGI_APPLICATION = 'testapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
