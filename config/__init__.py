class Config(object):

    # flask config
    FLASK_SECRET_KEY = "3d6f45a5fc12445dbac2f59c3b6c7cb1"

    # celery config
    CELERY_BROKER_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
