from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '^9cfg@ro4sybzb878&r%9fkfkwk1ja-u#0i&iy^_a&1#9hsmqp'

# SECURITY WARNING: define the correct hosts in production!
# ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'zappa_django_utils.db.backends.s3sqlite',
        'NAME': 'sqlite.db',
        'BUCKET': 'zappa-wagtail-drugsandme'
    }
}
