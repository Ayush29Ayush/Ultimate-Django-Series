from .common import *
import dj_database_url
import os

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': dj_database_url.config()
}