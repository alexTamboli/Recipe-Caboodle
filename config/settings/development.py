from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",  # Example: Your frontend application's address
#     "https://yourfrontenddomain.com",
#     # Add more origins as needed
# ]

# CORS_ALLOW_CREDENTIALS = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')