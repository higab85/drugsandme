from .base import *
from django.utils.translation import gettext_lazy as _

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = "7_@yl@!*7agyry-vg9ca5)e36eyympo0lcs+0=+%!etb!&6gj-"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }

}

LANGUAGES = [
  ('en', _('English')),
  ('es', _('Spanish')),
]
