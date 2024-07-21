release: python manage.py migrate
web: gunicorn storefront.wsgi
worker: celery -A storefront.celery worker --pool=solo -l info