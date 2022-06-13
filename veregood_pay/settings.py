"""
Django settings for veregood_pay project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-az*e41uu0kgt15!mp=%cgjsmtbca%d7zmqe753ijtekw7md_$r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

LIVE_MODE = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'setting',
    # 'service',
    # 'wallet',
    # 'payment',
    'account', # smart_card ( qr code )
    # 'finance', # banks (bank official website) ,
    # 'health',
    # 'job',
    # 'forum', #funding , ask funs , list funds , donate , create projects

    # # # additional
    # 'savings',
    # 'promotion',
    # 'electricity',
    # 'mobile_recharge',
    # 'trade',
    # 'dth',
    # 'recharge',
    # 'bill_payment',

    # restframework
    'rest_framework',
    'rest_framework.authtoken',

    # Socket
    'channels',
    'chat',
    

    # GEO-DJANGO
    'django.contrib.gis',
    'mapwidgets', # Google Map Widget
    'rest_framework_gis',


    # Veregood 
    'mptt',
    'veregood',
    'veregood_service',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication', 
    ],
     'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'veregood_pay.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

ASGI_APPLICATION = 'veregood_pay.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis://:AqqHx8XeuwW5pPrN2WJmUTaENrxpTJmN@redis-16027.c92.us-east-1-3.ec2.cloud.redislabs.com:16027')],
        },
    },
}



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db3.sqlite3',
#     }
# }

if LIVE_MODE == False:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'test1',
            'USER': 'dexternorman',
            'PASSWORD': 'Welcome123',
            'HOST': 'localhost',
            'PORT': '5432',
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'goodepay',
            'USER': 'dextern',
            'PASSWORD': 'Welcome123',
            'HOST': 'localhost',
            'PORT': '5432',
        },
    }

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8100', 'http://localhost',  'capacitor://localhost'
]  # If this is used, then not need to use `CORS_ORIGIN_ALLOW_ALL = True`
CORS_ORIGIN_REGEX_WHITELIST = [
    'http://localhost:8100', 'http://localhost', '*', 'capacitor://localhost'
]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd3md5oriiulc70',
#         'USER': 'jhezoguyazzhtz',
#         'PASSWORD': '64e755e259eb4b89bcdb3a216fb0c691ef29df6c535e466e67505e925f1defbc',
#         'HOST': 'ec2-3-226-165-146.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR,"static")

STATICFILES_DIRS = [os.path.join(BASE_DIR,"static")]

MEDIA_URL  = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media")
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AUTH USER MODEL 
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/

AUTH_USER_MODEL = 'account.User'


# https://docs.djangoproject.com/en/4.0/ref/contrib/gis/tutorial/
# Download URL http://download.osgeo.org  GDAL 2.2.2 , GEOS 3.3.0 , PROJ 4

GDAL_LIBRARY_PATH = "/usr/local/lib/libgdal.so"
# GEOS_LIBRARY_PATH = "/usr/local/lib/libgeos_c.so"


# Map Widgets settings 
# Documentation : https://readthedocs.org/projects/django-map-widgets/downloads/pdf/latest/

MAP_WIDGETS = {
"GooglePointFieldWidget": (
("zoom", 15),
("mapCenterLocationName", "london"),
("markerFitZoom", 12),
),
"GOOGLE_MAP_API_KEY": "AIzaSyAxW6RMgpC8nTMAmcYGcKsnd74PtT3QEh0"
}


STRIPE_WEBHOOK_SECRECT = "we_1KyIhtSHEdoMqgR5RzBYz8M5"
STRIPE_SECRECT         = "sk_test_51KPDPESHEdoMqgR5GfM94tXGSv1d09rc4KURnLDF3ETL0hZtYJbp89D1JMMd6jSEgQew29j6j7pj2vYKnuioVbb4004nbAp1vm"

