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
SECRET_KEY = config.get('deploy', 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if config.get('deploy', 'DEBUG') == "True":
    DEBUG = True
elif config.get('deploy', 'DEBUG') == "False":
    DEBUG = False

ALLOWED_HOSTS = [config.get('deploy', 'ALLOWED_HOSTS')]

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
    # 카운팅 모듈
    'hitcount',
    # 디버깅 툴바
    'debug_toolbar',
    # werkzeug 디버거를 위한 추가
    'django_extensions',
]

MIDDLEWARE_CLASSES = [
    # 디버깅 툴바 추가
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 기존코드
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

# switch whitenoise : CDN사용 여부에 따라 설정파일에서 whitenoise를 켜고 끌수있게 만들어준다.
if config.get('deploy', 'WHITENOISE') == 'True':
    # 'django.middleware.security.SecurityMiddleware'아래에 whitenoise 미들웨어 클래스가 위치해야 한다
    posithon = MIDDLEWARE_CLASSES.index('django.middleware.security.SecurityMiddleware') + 1
    MIDDLEWARE_CLASSES.insert(posithon, 'whitenoise.middleware.WhiteNoiseMiddleware')
elif config.get('deploy', 'WHITENOISE') == 'False':
    pass

ROOT_URLCONF = 'everpython.urls'
# 진자 기본 템플릿설정으로 변경
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': config.get('db', 'ENGINE'),
        'NAME': config.get('db', 'NAME'),
        'USER': config.get('db', 'USER'),
        'PASSWORD': config.get('db', 'PASSWORD'),
        'HOST': config.get('db', 'HOST'),
        'POST': config.get('db', 'POST'),
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
LANGUAGE_CODE = config.get('language', 'LANGUAGE_CODE')
TIME_ZONE = config.get('language', 'TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True

## 템플릿 파일 설정
TEMPLATES_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
# ckeditor 설정
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "uploads/"

# django jet 설정
if config.get('jet', 'SIDE_MENU') == "True":
    JET_SIDE_MENU_COMPACT = True
elif config.get('jet', 'SIDE_MENU') == "False":
    JET_SIDE_MENU_COMPACT = False
# 구글 웹로그 연동
JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = os.path.join(BASE_DIR, 'client_secrets.json')

# jet 대쉬보드 지정
JET_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
# JET_APP_INDEX_DASHBOARD = 'jet.dashboard.DefaultAppIndexDashboard'

# 디버깅 툴바 설정
INTERNAL_IPS = ['127.0.0.1', '::1']

# s3 설정
AWS_S3_HOST = config.get('s3', 'S3_HOST')
AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = config.get('s3', 'ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config.get('s3', 'SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config.get('s3', 'BUCKET')
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"

# 화이트노이즈 비활성화시 자동으로 s3를 collect-static 파일로 사용한다
if config.get('deploy', 'WHITENOISE') == 'False':
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATIC_ROOT = 'static'
    STATIC_URL = 'http://{0}.{1}/static/'.format(AWS_STORAGE_BUCKET_NAME,AWS_S3_HOST)

# 디스커스 설정
SHORTNAME = config.get('disqus', 'SHORTNAME')

# 구글 애드센스 설정
# 광고 게시 여부
try:
    AD_PAGE = True if config.get('googleAD', 'AD_PAGE') == 'True' else False
    AD_POSTTOP = True if config.get('googleAD', 'AD_POSTTOP') == 'True' else False
except:
    AD_PAGE, AD_POSTTOP = False, False

# 광고 스크립트 설정 정보
try:
    AD_CLIENT_ID = config.get('googleAD', 'AD_CLIENT')
    AD_SLOT_ID = config.get('googleAD', 'AD_SLOT')
except:
    AD_CLIENT_ID,AD_SLOT_ID = False,False
# 템플릿에서 처리할 광고 정보 취합
try:
    AD_STATE = {'page': AD_PAGE, 'top': AD_POSTTOP, 'client': AD_CLIENT_ID, 'slot': AD_SLOT_ID}
except:
    AD_STATE = False

# 구글 태그 매니저 설정
try:
    GTM = True if config.get('gtm', 'GTM') == 'True' else False
    GTM_ID = config.get('gtm', 'GTM_ID') if config.get('gtm', 'GTM_ID') else False
except:
    GTM, GTM_ID = False, False

GTM_STATE = {'state': GTM, 'id': GTM_ID}

# OG TAG 설정
try:
    OG_TAG = { 'name': config.get('og', 'NAME') , 'local': config.get('og', 'LOCAL'), 'img_url': config.get('og', 'IMG_URL'), 'img_type': config.get('og', 'IMG_TYPE'), 'img_width': config.get('og', 'IMG_WIDTH'), 'img_height': config.get('og', 'IMG_HEIGHT'), }
except:
    OG_TAG = { 'name': False, 'local': False, 'img_url': False, 'img_type': False, 'img_width':False, 'img_height': False, }


# CKEditor 설정
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_RESTRICT_BY_USER = True  # 사용자 별로 본인이 업로드한 이미지만 보이도록함

# ckeditor 설정
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'flat',
        # 'skin': 'moono,flat',
        'toolbar_Posting': [
            {'name': 'document', 'items': ['Source', 'Preview', '-', 'Find', 'Replace', 'SelectAll']},

            {'name': 'paragraph',
             'items': ['Image', 'Table', 'HorizontalRule', 'CodeSnippet', 'NumberedList', 'BulletedList', '-',
                       'Blockquote', 'CreateDiv']},
            {'name': 'insert',
             'items': ['Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            '/',
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'styles', 'items': ['Styles', 'Format', 'FontSize']},
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
        ],
        'toolbar': 'Posting',
        'codeSnippet_theme': 'monokai_sublime',
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                # your extra plugins here
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                # 'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
                'codesnippet'
            ]),
    }
}
