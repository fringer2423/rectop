from celery import shared_task


@shared_task
def create_task(task_type):
    result = 0
    for i in range(1000000000 * task_type):
        result += i
    return result
