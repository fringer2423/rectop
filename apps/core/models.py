import os

from pytils import translit

from datetime import datetime, timedelta

from django.db import models
from django.urls import reverse
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
    """
    Модель пользователя платформы
    """

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')
    location = models.CharField(max_length=30, null=True, blank=True, verbose_name='Страна')
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')
    verify_code = models.CharField(max_length=80, null=True, blank=True, verbose_name='Проверочный код')
    rate = models.CharField(max_length=30, null=True, blank=True, verbose_name='Тариф')
    job_title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Должность')

    def __str__(self):
        return self.get_full_name()


class Company(models.Model):
    """
    Модель компании, которую создает пользователь
    """

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', related_name='companies')
    name = models.CharField(max_length=100, verbose_name='Название компании')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """
    Модель для хранения графика работы филиалов
    """
    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'

    monday_start = models.TimeField(verbose_name='Начало работы в Понедельник')
    monday_end = models.TimeField(verbose_name='Окончание работы в Понедельник')
    monday_day_off = models.BooleanField(default=False, verbose_name='Понедельник выходной')
    tuesday_start = models.TimeField(verbose_name='Начало работы во Вторник')
    tuesday_end = models.TimeField(verbose_name='Окончание работы во Вторник')
    tuesday_day_off = models.BooleanField(default=False, verbose_name='Вторник выходной')
    wednesday_start = models.TimeField(verbose_name='Начало работы в Среду')
    wednesday_end = models.TimeField(verbose_name='Окончание работы в Среду')
    wednesday_day_off = models.BooleanField(default=False, verbose_name='Среда выходной')
    thursday_start = models.TimeField(verbose_name='Начало работы в Четверг')
    thursday_end = models.TimeField(verbose_name='Окончание работы в Четверг')
    thursday_day_off = models.BooleanField(default=False, verbose_name='Четверг выходной')
    friday_start = models.TimeField(verbose_name='Начало работы в Пятницу')
    friday_end = models.TimeField(verbose_name='Окончание работы в Пятницу')
    friday_day_off = models.BooleanField(default=False, verbose_name='Пятница выходной')
    saturday_start = models.TimeField(verbose_name='Начало работы в Субботу')
    saturday_end = models.TimeField(verbose_name='Окончание работы в Субботу')
    saturday_day_off = models.BooleanField(default=False, verbose_name='Суббота выходной')
    sunday_start = models.TimeField(verbose_name='Начало работы в Воскресенье')
    sunday_end = models.TimeField(verbose_name='Окончание работы в Воскресенье')
    sunday_day_off = models.BooleanField(default=False, verbose_name='Воскресенье выходной')


class Branch(models.Model):
    """
    Модель филиала
    """
    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания', related_name='branchs')
    name = models.CharField(max_length=100, verbose_name='Название')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE, verbose_name='График работы')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    description = models.TextField(verbose_name='Описание')
    short_description = models.TextField(verbose_name='Короткое описание')
    last_date_load_reviews = models.DateTimeField(default=datetime.now() - timedelta(hours=13))

    def __str__(self):
        return self.name


class Telebot(models.Model):
    """
    Модель для хранения настроек telegram уведомлений
    """
    class Meta:
        verbose_name = 'Настройки отправки Telegram уведомлений'

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name='Филиал', related_name='telebot_settings')
    tg_id = models.CharField(max_length=100, verbose_name='ID в Telegram')

    def __str__(self):
        return f'Настройка для {self.branch.name}'


class QRCode(models.Model):
    """
    Модель для хранения QRCodes
    """
    class Meta:
        verbose_name = 'QRCode'
        verbose_name_plural = 'QRCodes'

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name='Филиал', related_name='QRCode')
    slug_name = models.SlugField(max_length=200, db_index=True, blank=True, unique=True, verbose_name='URL')

    def save(self, *args, **kwargs):
        branch_name = f'{self.branch.name}_{self.branch.id}'
        self.slug_name = translit.slugify(branch_name)
        super().save(*args, **kwargs)


class Connect(models.Model):
    """
    Модель для настроек соединения с платформами
    """
    class Meta:
        verbose_name = 'Настройка соединения'
        verbose_name_plural = 'Настройки соединения'

    PLATFORMS_LIST = [
        (0, 'Yandex'),
        (1, '2GIS'),
        (2, 'Google'),
        (3, 'Flamp'),
        (4, 'Zoon'),
        (5, 'Yell')]

    type = models.CharField(max_length=20, choices=PLATFORMS_LIST, verbose_name='Платформа')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания')
    key = models.CharField(max_length=100, verbose_name='Ключ для подключения')

    def __str__(self):
        return f'Настройка подключения к платформе {self.type} для {self.company.name}'


class Review(models.Model):
    """
    Модель отзывов
    """
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    LIST_OF_RATINGS = [
        (0, 'Очень плохо'),
        (1, 'Плохо'),
        (2, 'Неплохо'),
        (3, 'Средне'),
        (4, 'Хорошо'),
        (5, 'Отлично')]

    STATUS_LIST = [
        (0, 'Не прочитано'),
        (1, 'Прочитано'),
        (2, 'С ответом'),
    ]

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name='Филиал')
    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    link = models.CharField(max_length=200, verbose_name='Ссылка')
    status = models.CharField(max_length=20, choices=STATUS_LIST, default=0, verbose_name='Статус')
    rating = models.CharField(max_length=20, choices=LIST_OF_RATINGS, verbose_name='Оценка')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True, blank=True)
    answered_at = models.DateTimeField(verbose_name='Дата ответа', null=True, blank=True)

    def __str__(self):
        return self.full_name


class ReviewSettings(models.Model):
    """
    Модель для хранения и управления настройками автоответов на отзывы
    """
    class Meta:
        verbose_name = 'Настройка автоответов на отзывы'

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='review_settings', verbose_name='Филиал')
    mask = models.TextField(verbose_name='Маска для отзыва')

    def __str__(self):
        return f'Настройка отзывов для {self.branch.name}'


class Answer(models.Model):
    """
    Модель для хранения ответов на отзывы
    """
    class Meta:
        verbose_name = 'Ответ на отзыв'
        verbose_name_plural = 'Ответы на отзывы'

    TYPE_LIST = [
        (0, 'Ответ создан автоматически'),
        (1, 'Ответ от пользователя')
    ]

    review = models.OneToOneField(Review, on_delete=models.CASCADE, verbose_name='Отзыв', related_name='answer')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True, blank=True)
    body = models.TextField(verbose_name='Ответ на отзыв')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers', verbose_name='Пользователь')
    type = models.CharField(max_length=100, choices=TYPE_LIST, verbose_name='Тип ответа')

    def __str__(self):
        return f'Ответ на отзыв {self.review.full_name}'
