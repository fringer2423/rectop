import os

from celery import Celery
from celery.signals import setup_logging

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'discovery_of_new_branches_task': {
        'task': 'discovery_of_new_branches_task',
        'schedule': 30.0,
        'options': {
            'queue': 'periodic',
        },
    },
}
app.conf.timezone = 'Europe/Moscow'


@setup_logging.connect
def config_loggers(*args, **kwargs) -> None:
    from logging.config import dictConfig
    from django.conf import settings

    dictConfig(settings.LOGGING)
