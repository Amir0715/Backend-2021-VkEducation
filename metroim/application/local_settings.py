DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb',
        'USER': 'djangouser',
        'PASSWORD': 'root123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

SOCIAL_AUTH_GITHUB_KEY = '27536f4c9c1279f88cc4'
SOCIAL_AUTH_GITHUB_SECRET = '1eb6fc5cacd275ff12942a38403e89ecfe95160c'

EMAIL_HOST_USER = 'amir.kamolov2000@gmail.com'
DEFAULT_FROM_EMAIL = 'amir.kamolov2000@gmail.com'
EMAIL_HOST_PASSWORD = 'acgwwsypawisyjdd'

ADMINS = ['kamolov.amir2000@yandex.ru']
