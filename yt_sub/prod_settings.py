from .settings import *
import dj_database_url

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
DEBUG = True

DATABASES = {
    'default': dj_database_url.config()
}
