import os

from django.db import models
from django.contrib.auth.models import AbstractUser


def my_awesome_upload_function(instance, filename):
    """
    Функция, преобразовывающая путь к файлу.
    :param instance: Объект.
    :param filename: Имя файла.
    :return: путь к файлу, для сохранения в БД.
    """
    return os.path.join('media/avatars/{}/'.format(instance.get_directory()), filename)


class User(AbstractUser):
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')
    location = models.CharField(max_length=30, null=True, blank=True, verbose_name='Страна')

    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')

    def __str__(self):
        return self.get_full_name()
