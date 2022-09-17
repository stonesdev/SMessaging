from datetime import date, datetime

from django.core.files.storage import FileSystemStorage

from .base_settings import *

# DEBUG = int(os.environ.get('DEBUG', default=1))
DEBUG = True

CUSTOM_DOMAIN_NAME = 'Core'
ALLOWED_HOSTS = ['*', '127.0.0.1']

# Host Backend urls
CUSTOM_BACKEND_SITE_URL = 'http://localhost:8000'
CUSTOM_IMAGES_HOST_URL = CUSTOM_BACKEND_SITE_URL  # CUSTOM_BACKEND_SITE_URL  # CUSTOM_BACKEND_SITE_URL
# Host Frontend urls
CUSTOM_FRONTEND_SITE_URL = 'http://localhost:4200'
CUSTOM_PASSWORD_RESET_PAGE_URL = CUSTOM_FRONTEND_SITE_URL + '/auth/set/password-confirm-reset/confirm'

CUSTOM_ACCOUNT_CONFIRM_EMAIL_URL = CUSTOM_FRONTEND_SITE_URL + "/auth/set/account-confirm-email/?key={0}"

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

