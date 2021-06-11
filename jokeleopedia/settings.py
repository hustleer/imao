"""
Django settings for jokeleopedia project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""



import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&kz+!2-30i1ld$(dx1$joifq$8ll3_b)_=ep-0o0bcx#-w^5yy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['imao.herokuapp.com','127.0.0.1','0.0.0.0', 'https://imao.herokuapp.com/chit-chat/mermaid/']


# Application definition

INSTALLED_APPS = [
    'channels',     #For chit-chat
    'jokes.apps.JokesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'ariesap.apps.AriesapConfig',
    #'memmes.apps.MemmesConfig',
    'memes.apps.MemesConfig',
    'user.apps.UserConfig',
    'chat.apps.ChatConfig',
    'cos.apps.CosConfig',
    'hotornot.apps.HotornotConfig',
    'django.contrib.sitemaps',  # For sitemaps
    'django.contrib.sites',
]
SITE_ID=1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',#For Static files
]

ROOT_URLCONF = 'jokeleopedia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #to tell Django to look for a templates folder at the project level. 
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'jokeleopedia.wsgi.application'

###################- For Chat -##################################
# Channels

ASGI_APPLICATION = 'jokeleopedia.asgi.application'
CHANNEL_LAYERS = {
"default": {
'BACKEND': 'channels_redis.core.RedisChannelLayer',
         'CONFIG': {
             "hosts": [
               'redis://h:mgvo5Wtn15X24E6oy2p5taLyYcRDaHBd@redis-15253.c1.ap-southeast-1-1.ec2.cloud.redislabs.com:15253'
               #'redis://h:le16Dn6dYwGHOZLF9vWxySxmQSIwE4Zz@redis-12573.c99.us-east-1-4.ec2.cloud.redislabs.com:12573' 
               #'redis://h:<password>;@<redis Endpoint>:<port>' 
             ],
             "symmetric_encryption_keys": ['&kz+!2-30i1ld$(dx1$joifq$8ll3_b)_=ep-0o0bcx#-w^5yy'],
         },
         }}


'''CHANNEL_LAYERS = {
"default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    },
    
    'with_redis': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            #"hosts": [('127.0.0.1', 6379)],
            #"hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379',)],
            'HOST':['ec2.cloud.redislabs.com',15253],
            'PASSWORD':'mgvo5Wtn15X24E6oy2p5taLyYcRDaHBd',
            'PORT':15253,
        },
    },
}'''
#redis-15253.c1.ap-southeast-1-1.ec2.cloud.redislabs.com:15253

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ukcaqslx',
        'USER': 'ukcaqslx',
        'PASSWORD': 'q4dsyK-YwAZodwE8vaqkU0n79B3ae8_O',
        'HOST': 'ziggy.db.elephantsql.com',
        'PORT': '5432',
    },
    'imgflip_memes': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'amfzthmk',
        'USER': 'amfzthmk',
        'PASSWORD': 'WjJScOKRbWv9bslRZLL-mR6lmFYJPaKx',
        'HOST': 'john.db.elephantsql.com',
        'PORT': '5432',
    },
    
    'user_uploaded': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ptcykkpi',
        'USER': 'ptcykkpi',
        'PASSWORD': 'GbX5r-Sf7Tyb-UkCWIBpuBShr-snFnPP',
        'HOST': 'john.db.elephantsql.com',
        'PORT': '5432',
    },
        
    'stupidstuff_jokes': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ufxksnan',
        'USER': 'ufxksnan',
        'PASSWORD': 'FrzEtent9obJ7NcW_UOgjSPA4xK6aqA-',
        'HOST': 'arjuna.db.elephantsql.com',
        'PORT': '5432',
    },
    'reddit_jokes': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sbcwfsyk',
        'USER': 'sbcwfsyk',
        'PASSWORD': 'T7whneqWgyy9XiFf-SLFiJIqubfK_2Go',
        'HOST': 'john.db.elephantsql.com',
        'PORT': '5432',
    },
    'reddit_second': {#google hong kong
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mvtaovkz',
        'USER': 'mvtaovkz',
        'PASSWORD': 'NJv5lwVb4MjLsFZkRNqWrD9PLDMfhHO-',
        'HOST': 'satao.db.elephantsql.com',
        'PORT': '5432',
    },
    'reddit_third': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sbcwfsyk',
        'USER': 'sbcwfsyk',
        'PASSWORD': 'T7whneqWgyy9XiFf-SLFiJIqubfK_2Go',
        'HOST': 'john.db.elephantsql.com',
        'PORT': '5432',
    },
    'reddit_fourth': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sbcwfsyk',
        'USER': 'sbcwfsyk',
        'PASSWORD': 'T7whneqWgyy9XiFf-SLFiJIqubfK_2Go',
        'HOST': 'john.db.elephantsql.com',
        'PORT': '5432',
    },
    'reddit_fifth': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sbcwfsyk',
        'USER': 'sbcwfsyk',
        'PASSWORD': 'T7whneqWgyy9XiFf-SLFiJIqubfK_2Go',
        'HOST': 'john.db.elephantsql.com',
        'PORT': '5432',
    },
    'reddit_best': {#AWS HongKong faster than AWS tokyo and Google HongKong
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pyxtubqz',
        'USER': 'pyxtubqz',
        'PASSWORD': 'V-TYYdGyKWRT_hh3v66yuVUsx0o9aiVC',
        'HOST': 'john.db.elephantsql.com',
        'PORT': '5432',
    },
    'feedbacks': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jpyjlpub',
        'USER': 'jpyjlpub',
        'PASSWORD': 'g1tXihTP_-tdECcH1SX1BSo9isiQ7bG8',
        'HOST': 'john.db.elephantsql.com',
        'PORT': '5432',
    },
    'jokes': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gmpydomg',
        'USER': 'gmpydomg',
        'PASSWORD': 'jWqgyDOz7ROAuj2ENryWiBGIpZwrODZG',
        'HOST': 'john.db.elephantsql.com',
        'PORT': '5432',
    },

}




'''
'''
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
import os
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join('BASE_DIR','staticfiles')

#For Seding mail:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = 'amaryesh123456@gmail.com'
EMAIL_HOST_PASSWORD = 'password'         # username and password
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'amaryesh123456@gmail.com'
SERVER_EMAIL = 'amaryesh123456@gmail.com'

#For login redirect page
#LOGIN_REDIRECT_URL = '/user/info/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/jokes/'
#REGISTER_REDIRECT_URL = '/user/info/'
# Real-world : integrate with an email service like MailGun or SendGrid
# django allows to store emails either in the console or as a file.
# To store as File:
#EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
#EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))


###########For static Files#################
#source:https://devcenter.heroku.com/articles/django-assets
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


#Finally, if you’d like gzip functionality enabled, also add the following setting to settings.py.
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


