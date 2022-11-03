import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'discovery_of_new_branches_task': {
        'task': 'discovery_of_new_branches_task',
        'schedule': 30.0,
    },
}
app.conf.timezone = 'Europe/Moscow'
