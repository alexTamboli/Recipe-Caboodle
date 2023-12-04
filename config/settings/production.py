from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', '.now.sh']

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