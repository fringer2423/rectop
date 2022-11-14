import logging

from celery import shared_task

from config.celery import app

from .services.periodic_tasks_service import discovery_of_new_branches_service


@app.task(name='discovery_of_new_branches_task')
def discovery_of_new_branches_task(*args):
    """Задача для поиска новых филиалов"""
    logger = logging.getLogger('celery')
    logger.warning('CELERY!!!!')
    return discovery_of_new_branches_service()
