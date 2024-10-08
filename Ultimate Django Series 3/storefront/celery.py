# import os
# from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')

# celery = Celery('storefront')
# celery.config_from_object('django.conf:settings', namespace='CELERY')
# celery.autodiscover_tasks()   

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings.dev')

celery = Celery('storefront')
celery.config_from_object(settings, namespace='CELERY')
celery.autodiscover_tasks()