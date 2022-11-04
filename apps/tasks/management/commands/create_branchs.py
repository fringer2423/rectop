import random
import string
import time

from django.core.management.base import BaseCommand
from django.conf import settings
from apps.core.models import Branch, Connect

letters = string.ascii_letters
numbers = string.digits


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        for _ in range(1000):
            branch = Branch.objects.create(
                name=''.join(random.choice(letters) for i in range(10)),
                company_id=1
            )
            Connect.objects.create(
                branch_id=branch.id,
                type=2,
                key='1231',
            )

