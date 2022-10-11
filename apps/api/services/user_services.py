from django.contrib.auth.hashers import make_password

from apps.core.models import User


def create_user(data):
    user = User.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        # username=data['email'],
        email=data['email'],
        password=make_password(data['password'])
    )
    return user
