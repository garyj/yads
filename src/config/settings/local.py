from config.settings.base import *

# add local hosts to ALLOWED_HOSTS, 0.0.0.0 will bind to all interfaces
ALLOWED_HOSTS = [*ALLOWED_HOSTS, 'localhost', '0.0.0.0', '127.0.0.1', '{{ project_name }}.local']  # noqa: S104

# in local we use Whitenoise to server static files as we use uvicorn in development
sec_middleware_index = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware')
MIDDLEWARE.insert(sec_middleware_index + 1, 'whitenoise.middleware.WhiteNoiseMiddleware')


# STATIC Config closer mimic to production using whitenoise and ManifestStaticFilesStorage
# this is tested via `compose-prod.yaml`
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
