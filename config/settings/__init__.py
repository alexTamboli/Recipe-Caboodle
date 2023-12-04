from .base import *
import os

print(os.getenv("ENVIRONMENT"))

if os.environ.get("ENVIRONMENT") == 'Production':
    from .production import *
else:
    from .development import *
