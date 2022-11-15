import logging

from celery import shared_task

from config.celery import app

from .services.periodic_tasks_service import discovery_of_new_branches_service
from .services.email_service import send_email_service


@app.task(name='discovery_of_new_branches_task')
def discovery_of_new_branches_task(*args):
    """Задача для поиска новых филиалов"""
    logger = logging.getLogger('celery')
    logger.warning('CELERY!!!!')
    return discovery_of_new_branches_service()


@shared_task(queue='email_push')
def send_email_task(subject, body, email):
    logger = logging.getLogger('celery')
    logger.warning('EMAIL!!!!')
    return send_email_service(subject, body, email)
