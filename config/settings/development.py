from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CORS_ORIGIN_ALLOW_ALL = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')