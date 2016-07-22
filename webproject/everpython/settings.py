# -*- coding: utf-8 -*-

"""
Django settings for everpython project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ini파일 호출
from configparser import RawConfigParser
config = RawConfigParser()
config.read(os.path.join(BASE_DIR, 'settings.ini'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('deploy','SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if config.get('deploy','DEBUG') == "True":
    DEBUG = True
elif config.get('deploy','DEBUG') == "False":
    DEBUG = False

ALLOWED_HOSTS = [config.get('deploy','ALLOWED_HOSTS')]


# Application definition

INSTALLED_APPS = [
    # django jet admin
    'jet.dashboard',
    'jet',
    # django base admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ckeditor
    'ckeditor',
    'ckeditor_uploader',
    # storages
    'storages',
    # 태그
    'taggit',
    # 블로그앱 추가
    'blog',
    # 장고용 진자
    'django_jinja',
    'django_jinja.contrib._humanize',
    # 카운팅 모듈
    'hitcount',
    # 디버깅 툴바
    'debug_toolbar',
]

MIDDLEWARE_CLASSES = [
    # 디버깅 툴바 추가
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 기존코드
    'django.middleware.security.SecurityMiddleware',
    # whitnoise
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # 기존 코드
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]
'''
if config.get('deploy','WHITENOISE')=='True':
    MIDDLEWARE_CLASSES 'whitenoise.middleware.WhiteNoiseMiddleware',
elif config.get('deploy','WHITENOISE')=='False':
    pass
'''
ROOT_URLCONF = 'everpython.urls'
# 진자 기본 템플릿설정으로 변경
TEMPLATES = [
    {
        'BACKEND': "django_jinja.backend.Jinja2",
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'everpython.jinja2.environment',
            "app_dirname": "templates",
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'everpython.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': config.get('db','ENGINE'),
        'NAME': config.get('db','NAME'),
        'USER': config.get('db','USER'),
        'PASSWORD': config.get('db','PASSWORD'),
        'HOST': config.get('db','HOST'),
        'POST': config.get('db','POST'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# 한국 설정
LANGUAGE_CODE = config.get('language','LANGUAGE_CODE')
TIME_ZONE = config.get('language','TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True


## 템플릿 파일 설정
TEMPLATES_DIRS=[os.path.join(BASE_DIR,'templates')]
# ckeditor 설정
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "uploads/"


# django jet 설정
if config.get('jet','SIDE_MENU') == "True":
    JET_SIDE_MENU_COMPACT = True
elif config.get('jet','SIDE_MENU') == "False":
    JET_SIDE_MENU_COMPACT = False
# 구글 웹로그 연동
JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = os.path.join(BASE_DIR, 'client_secrets.json')

# jet 대쉬보드 지정
JET_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
#JET_APP_INDEX_DASHBOARD = 'jet.dashboard.DefaultAppIndexDashboard'

# 디버깅 툴바 설정
INTERNAL_IPS = ['127.0.0.1','::1']

# s3 설정
AWS_S3_HOST = config.get('s3','S3_HOST') # 서울 리전
AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = config.get('s3','ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config.get('s3','SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config.get('s3','BUCKET')
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"