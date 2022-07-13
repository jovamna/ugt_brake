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
    'direccion ip', 'localhost', 'www.ugtjjuanbs.com', 'ugtjjuanbs.com'
]

SECRET_KEY = env.str('SECRET_KEY')



# Database
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
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = (BASE_DIR,'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




#email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
#EMAIL_USE_TLS = False