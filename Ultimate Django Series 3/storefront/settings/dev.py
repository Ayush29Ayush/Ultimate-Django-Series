from .common import *

SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': 'localhost', #! This was used without docker
        # 'HOST': 'mysql', #! This is used with docker as per the name in the docker-compose.yml 
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Ab@123456'
    }
}

CELERY_BROKER_URL = 'redis://localhost:6379/1' #! This was used without docker
# CELERY_BROKER_URL = 'redis://redis:6379/1' #! This is used with docker as per the name in the docker-compose.yml

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2", #! This was used without docker
        # "LOCATION": "redis://redis:6379/2", #! This is used with docker as per the name in the docker-compose.yml
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "TIMEOUT": 10 * 60, #! 10 minutes
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'localhost' #! This was used without docker
# EMAIL_HOST = 'smtp4dev' #! This is used with docker as per the name in the docker-compose.yml
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}