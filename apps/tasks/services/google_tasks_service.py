import random
import string
import time

from celery import shared_task

from apps.api.services.branch_service import get_branch_by_id_service
from apps.api.services.review_service import create_review_by_branch_id_service
from apps.api.services.connect_service import get_connect_by_id_branch_and_type

letters = string.ascii_letters
numbers = string.digits


@shared_task
def first_download_of_branch_information_task(user, branch_id):
    branch = get_branch_by_id_service(user=user, branch_id=branch_id)
    branch.name = ''.join(random.choice(letters) for i in range(10))
    time.sleep(5)
    branch.address = ''.join(random.choice(letters) for i in range(10))
    time.sleep(5)
    branch.phone_number = ''.join(random.choice(numbers) for i in range(10))
    time.sleep(5)
    branch.email = ''.join(random.choice(letters) for i in range(10)) + '@' + ''.join(
        random.choice(letters) for i in range(5)) + '.ru'
    time.sleep(5)
    branch.description = ''.join(random.choice(letters) for i in range(10))
    time.sleep(5)
    branch.short_description = ''.join(random.choice(letters) for i in range(10))
    time.sleep(5)
    branch.save()
    uploading_branch_reviews_task.delay(user, branch_id)
    return True


@shared_task
def uploading_branch_reviews_task(user, branch_id):
    connect = get_connect_by_id_branch_and_type(user=user, branch_id=branch_id, connect_type=2)
    for i in range(100):
        create_review_by_branch_id_service(
            user=user,
            branch_id=branch_id,
            full_name=''.join(random.choice(letters) for i in range(10)),
            link=''.join(random.choice(letters) for i in range(10)),
            rating=5,
            connect_id=connect.id
        )
        time.sleep(2)
    return True


@shared_task
def leave_a_reply_to_a_review_task(user, review_id):
    time.sleep(15)
    return True
