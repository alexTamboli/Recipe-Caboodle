from .base import *

DEBUG = False
ALLOWED_HOSTS = ['recipe-caboodle-backend-server.onrender.com']


CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'https://jovial-strudel-706543.netlify.app',
    'jovial-strudel-706543.netlify.app',
]

CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_HEADERS = (
#     'access-control-allow-credentials',
#     'access-control-allow-headers',
#     'access-control-allow-methods',
#     'access-control-allow-origin',
#     'content-type',
# )

INSTALLED_APPS += [
    'cloudinary_storage',
    'cloudinary',
]

# Media
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Cloudinary configs
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET')
}