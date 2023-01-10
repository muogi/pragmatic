from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '../../.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pinterestdb',
        'USER': 'root',
        'PASSWORD': '1q2w3e4r',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}