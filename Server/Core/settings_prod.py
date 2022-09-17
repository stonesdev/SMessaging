
from datetime import date, datetime

from .base_settings import *

DEBUG = False
try:
    # pyright: reportMissingImports=false
    import dj_database_url
 
    # define postgrel database connections
    db_from_env = dj_database_url.config()
    DATABASES['default'].update(db_from_env)
    DATABASES['default']['CONN_MAX_AGE'] = 500
    print('<------------ USING PRODUCTION SETTINGS ------------>')

except Exception:
    print('refused production environment')
    pass
    # logging.error('<------------ THIS ENVIRONMENT IS NOT AVAILABLE ------------>') vv

CUSTOM_DOMAIN_NAME = 'https://smessaging.com'  # 'https://docking-adventurebookings.herokuapp.com'
HEROKU_DOMAIN = 'https://docking-smessaging.herokuapp.com'
ALLOWED_HOSTS = [HEROKU_DOMAIN, CUSTOM_DOMAIN_NAME, '.herokuapp.com', 'www.smessaging.com', 'smessaging.com']
# Host Backend urls
CUSTOM_BACKEND_SITE_URL = CUSTOM_DOMAIN_NAME
CUSTOM_IMAGES_HOST_URL = ''  # CUSTOM_BACKEND_SITE_URL
# Host Frontend urls
CUSTOM_FRONTEND_SITE_URL = CUSTOM_DOMAIN_NAME
# Links
CUSTOM_PASSWORD_RESET_PAGE_URL = CUSTOM_FRONTEND_SITE_URL + '/auth/account/password-confirm-reset/confirm'
CUSTOM_ACCOUNT_CONFIRM_EMAIL_URL = CUSTOM_FRONTEND_SITE_URL + "/auth/account-confirm-email/?key={0}"
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
