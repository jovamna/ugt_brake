from pathlib import Path
import os
import environ


from django.conf import settings

settings.configure(
# ...
    ROOT_URLCONF=__name__,
# ...
    ),






env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-2z^%m3-@eagh!obvrz^hjgr-zy2b*8j2owl7hshuuf_mkn0e6m'
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'descargas',
    'comitiva',
    'contacto',
    'formacion',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        #'DIRS': [os.path.join(BASE_DIR, 'templates')],
        #'DIRS': [
    #'C:/Users/jjmed/OneDrive/Escritorio/Proyectos/ugt_brake/templates'
                   #],
                   
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  #para descaragr archivos
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'




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

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True

from django.utils.translation import gettext_lazy as _
LANGUAGES = (
    ('es', _('Español')),
    ('ca', _('Catalan')),
)

LOCALE_PATHS = (
    'C:/Users/jjmed/OneDrive/Escritorio/Proyectos/ugt_brake/locale',
    #os.path.join(BASE_DIR, 'locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
#STATICFILES_DIRS = (os.path.join( 'ugt_brake/static/'),)
#STATICFILES_DIRS = [BASE_DIR / 'static',]

#STATIC_ROOT = 'C:/Users/jjmed/OneDrive/Escritorio/Proyectos/ugt_brake/static'






#STATIC_URL = '/static/'
#descargar archivos
#MEDIA_URL = '/media/'
#STATICFILES_DIRS= [
    #'C:/Users/jjmed/OneDrive/Escritorio/Proyectos/ugt_brake/static',
                   #]
#MEDIA_ROOT = 'C:/Users/jjmed/OneDrive/Escritorio/Proyectos/ugt_brake/media',



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

