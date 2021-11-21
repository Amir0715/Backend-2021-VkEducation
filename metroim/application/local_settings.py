# DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'metroim',
        'USER': 'django_user',
        'PASSWORD': 'django_user',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}