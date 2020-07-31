from celery.schedules import crontab


DEBUG = False

SERVER_NAME = 'fourparts.herokuapp.com'
SECRET_KEY = '6ddf3179-9634-44b8-90af-6c741ab40b82'

STORE_PATH = 'fourpartsweb/storage/'
MIDISTORE_PATH = STORE_PATH + 'midifiles/'
PARALLEL_RESULTS_PATH = STORE_PATH + 'parallel_results/'
CHORD_RESULTS_PATH = STORE_PATH + 'chord_results/'

# USER
# PASSWORD
# DB

db_uri = 'postgres://pddovxouxdhfts:8fc7ca66a729d2fb2f58efe2b2d8e83abe055ec5be827edc0677983905f879e0@ec2-54-159-138-67.compute-1.amazonaws.com:5432/dc3cihr5l0c5ao'

SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Celery.
REDIS_PASSWORD = 'insert secure redis password here'
CELERY_BROKER_URL = 'redis://:{}@redis:6379/0'.format(REDIS_PASSWORD)
CELERY_RESULT_BACKEND = 'redis://:{}@redis:6379/0'.format(REDIS_PASSWORD)
CELERY_REDIS_MAX_CONNECTIONS = 5
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'clean_db-every-month': {
        'task': 'clean_db',
        'schedule': crontab(0, 0, day_of_month='1')
    }
}
