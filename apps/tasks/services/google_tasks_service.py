import random
import string
import time

from celery import shared_task

from apps.api.services.branch_service import get_branch_service
from apps.api.services.review_service import create_review_by_branch_id_service
from apps.api.services.connect_service import get_connect_by_id_branch_and_type
from apps.api.services.user_services import get_user_service

letters = string.ascii_letters
numbers = string.digits


@shared_task
def first_download_of_branch_information_task(branch_id):
    branch = get_branch_service(branch_id=branch_id)
    branch.is_detected = True
    branch.save()
    branch.name = ''.join(random.choice(letters) for i in range(10))

    branch.address = ''.join(random.choice(letters) for i in range(10))

    branch.phone_number = ''.join(random.choice(numbers) for i in range(10))

    branch.email = ''.join(random.choice(letters) for i in range(10)) + '@' + ''.join(
        random.choice(letters) for i in range(5)) + '.ru'

    branch.description = ''.join(random.choice(letters) for i in range(10))

    branch.short_description = ''.join(random.choice(letters) for i in range(10))

    branch.save()
    user_id = branch.company.owner_id
    uploading_branch_reviews_task.delay(user_id=user_id, branch_id=branch_id)
    return f'Филиал {branch.name} успешно обработан'


@shared_task
def uploading_branch_reviews_task(user_id, branch_id):
    user = get_user_service(user_id=user_id)
    connect = get_connect_by_id_branch_and_type(user=user, branch_id=branch_id, connect_type=2)
    if connect is None:
        raise Exception(f'Connect не найден для branch_id {branch_id}')
    for i in range(1000):
        create_review_by_branch_id_service(
            user=user,
            branch_id=branch_id,
            full_name=''.join(random.choice(letters) for i in range(10)),
            link=''.join(random.choice(letters) for i in range(10)),
            rating=5,
            connect_id=connect.id
        )

    return f'Успешно загружены 100 отзывов для branch_id {branch_id}'


@shared_task
def leave_a_reply_to_a_review_task(user, review_id):
    time.sleep(15)
    return True
