from django.db.models.signals import pre_save, post_save
from .models import User


def updateUser(sender, instance, **kwargs):
    """Сигнал, который перед сохранением User заменяет его username на email, если он есть"""
    user = instance
    if user.email != '':
        user.username = user.email


pre_save.connect(updateUser, sender=User)
