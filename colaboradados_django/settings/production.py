from decouple import config
from dj_database_url import parse as db_url

from .base import *

DEBUG = False

DATABASES = {
    'default': config('DATABASE_URL', default='', cast=db_url),
}
