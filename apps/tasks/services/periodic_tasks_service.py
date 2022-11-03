import time

from apps.api.services.branch_service import get_all_not_detected_branch_service
from .google_tasks_service import first_download_of_branch_information_task


def discovery_of_new_branches_service(*args):
    branch_list = get_all_not_detected_branch_service()
    for branch in branch_list:
        first_download_of_branch_information_task.delay(branch_id=branch.id)
    return f'Обнаружено и обработано {branch_list.count()}'
