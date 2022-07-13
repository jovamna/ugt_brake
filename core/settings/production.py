import os
import environ

env = environ.Env()
environ.Env.read_env()

from core.settings.base import *

DEBUG = False

#env = environ.Env(ALLOWED_HOSTS=(list, ['*',]),
# SECRET_KEY=str,
#)

ALLOWED_HOSTS = [
    #direccion ip'', 'localhost', 'www.ugtjjuanbs.com', 'ugtjjuanbs.com'
]

SECRET_KEY = env.str('SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRESQL_NAME'),
        'USER': env('POSTGRESQL_USER'),
        'PASSWORD': env('POSTGRESQL_PASS'),
        'HOST': env('POSTGRESQL_HOST'),
        'PORT': env('POSTGRESQL_PORT'),
    }
}



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
#CACHES = {
    #'default': {
        #'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        #'LOCATION': '127.0.0.1:11211',
        #'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        #'LOCATION': '127.0.0.1:11211',
    #}
#}



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#CON NGNIX
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = (BASE_DIR,'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]



#email config
#EMAIL_HOST = env('EMAIL_HOST')
#EMAIL_HOST_USER = env('EMAIL_HOST_USER')
#EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
#EMAIL_PORT = env('EMAIL_PORT')
#EMAIL_USE_TLS = True
