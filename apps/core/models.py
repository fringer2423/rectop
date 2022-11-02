import os

from pytils import translit

from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser


def my_awesome_upload_function(instance, filename):
    """
    Функция, преобразовывающая путь к файлу.
    :param instance: Объект.
    :param filename: Имя файла.
    :return: путь к файлу, для сохранения в БД.
    """
    return os.path.join('media/QRCodes/{}/'.format(instance.get_directory()), filename)


class User(AbstractUser):
    """
    Модель пользователя платформы
    """

    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    location = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name='Страна'
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name='Номер телефона'
    )
    verify_code = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        verbose_name='Проверочный код',
        unique=True
    )
    job_title = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Должность'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.get_full_name()} {self.id}'


class Rate(models.Model):
    """
    Модель тарифа
    """

    RATE_TYPE_CHOICES = [
        (0, 'Тестовый'),
        (1, 'Начальный'),
        (2, 'Средний'),
        (3, 'Профессиональный')
    ]

    number_of_branches = models.IntegerField(
        verbose_name='Количество филиалов',
        default=0
    )
    type = models.IntegerField(
        default=0,
        choices=RATE_TYPE_CHOICES
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='rate',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return f'Тариф {self.id}'


class Company(models.Model):
    """
    Модель компании, которую создает пользователь
    """

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        related_name='companies'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название компании'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class WorkDay(models.Model):
    """Модель рабочего дня"""
    DAYS_OF_WEEK_CHOICES = [
        (1, 'Понедельник'),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Четверг'),
        (5, 'Пятница'),
        (6, 'Суббота'),
        (7, 'Воскресенье'),
    ]
    DAY_TYPES_CHOICES = [
        ('weekday', 'Будний день'),
        ('holiday', 'Праздничный день'),
        ('day_off', 'Выходной')
    ]
    day_of_the_week = models.PositiveIntegerField(
        verbose_name='День недели',
        choices=DAYS_OF_WEEK_CHOICES
    )
    start_time = models.TimeField(
        verbose_name='Начало рабочего дня',
    )
    end_time = models.TimeField(
        verbose_name='Окончание рабочего дня',
        max_length=5
    )
    day_type = models.CharField(
        verbose_name='day type',
        max_length=255,
        choices=DAY_TYPES_CHOICES
    )

    class Meta:
        verbose_name = 'Рабочий день'
        verbose_name_plural = 'Рабочие дни'

    def __str__(self):
        return f'{self.get_day_of_the_week_display()} {self.get_day_type_display()}'


class Schedule(models.Model):
    """
    Модель для хранения графика работы филиалов
    """

    monday = models.ForeignKey(
        WorkDay,
        on_delete=models.CASCADE,
        verbose_name='Понедельник',
        related_name='monday',
        null=True,
        blank=True
    )
    tuesday = models.ForeignKey(
        WorkDay,
        on_delete=models.CASCADE,
        verbose_name='Вторник',
        related_name='tuesday',
        null=True,
        blank=True
    )
    wednesday = models.ForeignKey(
        WorkDay,
        on_delete=models.CASCADE,
        verbose_name='Среда',
        related_name='wednesday',
        null=True,
        blank=True
    )
    thursday = models.ForeignKey(
        WorkDay,
        on_delete=models.CASCADE,
        verbose_name='Четверг',
        related_name='thursday',
        null=True,
        blank=True
    )
    friday = models.ForeignKey(
        WorkDay,
        on_delete=models.CASCADE,
        verbose_name='Пятница',
        related_name='friday',
        null=True,
        blank=True
    )
    saturday = models.ForeignKey(
        WorkDay,
        on_delete=models.CASCADE,
        verbose_name='Суббота',
        related_name='saturday',
        null=True,
        blank=True
    )
    sunday = models.ForeignKey(
        WorkDay,
        on_delete=models.CASCADE,
        verbose_name='Воскресенье',
        related_name='sunday',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'

    def __str__(self):
        return f'График работы от {self.created_at.__format__("%Y-%m-%d %H:%M:%S")}'


class Branch(models.Model):
    """
    Модель филиала
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Компания',
        related_name='branchs'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    address = models.CharField(
        max_length=200,
        verbose_name='Адрес'
    )
    schedule = models.OneToOneField(
        Schedule,
        on_delete=models.CASCADE,
        verbose_name='График работы',
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    short_description = models.TextField(
        verbose_name='Короткое описание'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        null=True,
        blank=True
    )
    last_date_load_reviews = models.DateTimeField(
        default=datetime.now() - timedelta(hours=13),
        verbose_name='Последняя дата загрузки отзывов'
    )

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return f'{self.name} {self.id}'


class Telebot(models.Model):
    """
    Модель для хранения настроек telegram уведомлений
    """

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        verbose_name='Филиал',
        related_name='telebot_settings'
    )
    tg_id = models.CharField(
        max_length=100,
        verbose_name='ID в Telegram'
    )

    class Meta:
        verbose_name = 'Настройка отправки Telegram уведомлений'
        verbose_name_plural = 'Настройки отправки Telegram уведомлений'

    def __str__(self):
        return f'Настройка для {self.branch.name}'


class QRCode(models.Model):
    """
    Модель для хранения QRCodes
    """

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        verbose_name='Филиал',
        related_name='QRCode'
    )
    slug_name = models.SlugField(
        max_length=200,
        db_index=True,
        blank=True,
        unique=True,
        verbose_name='URL'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        null=True,
        blank=True
    )
    image = models.FileField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'QRCode'
        verbose_name_plural = 'QRCodes'

    def __str__(self):
        return f'QRCode для {self.branch.name}'

    def save(self, *args, **kwargs):
        branch_name = f'{self.branch.company.name}-{self.branch.name}-{self.branch.id}'
        self.slug_name = translit.slugify(branch_name)
        super().save(*args, **kwargs)


class Connect(models.Model):
    """
    Модель для настроек соединения с платформами
    """

    PLATFORMS_CHOICES = [
        (0, 'Yandex'),
        (1, '2GIS'),
        (2, 'Google'),
        (3, 'Flamp'),
        (4, 'Zoon'),
        (5, 'Yell')]

    type = models.CharField(
        max_length=20,
        choices=PLATFORMS_CHOICES,
        verbose_name='Платформа'
    )
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        verbose_name='Филиал'
    )
    key = models.CharField(
        max_length=100,
        verbose_name='Ключ для подключения'
    )
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Настройка соединения'
        verbose_name_plural = 'Настройки соединения'

    def __str__(self):
        return f'Настройка подключения к платформе {self.type} для {self.branch.name}'


class Review(models.Model):
    """
    Модель отзывов
    """

    RATINGS_CHOICES = [
        (0, 'Очень плохо'),
        (1, 'Плохо'),
        (2, 'Неплохо'),
        (3, 'Средне'),
        (4, 'Хорошо'),
        (5, 'Отлично')]

    STATUS_CHOICES = [
        (0, 'Не прочитано'),
        (1, 'Прочитано'),
        (2, 'С ответом'),
    ]

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        verbose_name='Филиал'
    )
    full_name = models.CharField(
        max_length=100,
        verbose_name='Полное имя'
    )
    link = models.CharField(
        max_length=200,
        verbose_name='Ссылка'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=0,
        verbose_name='Статус'
    )
    rating = models.CharField(
        max_length=20,
        choices=RATINGS_CHOICES,
        verbose_name='Оценка'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        null=True,
        blank=True
    )
    answered_at = models.DateTimeField(
        verbose_name='Дата ответа',
        null=True,
        blank=True
    )
    connect = models.ForeignKey(
        Connect,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.full_name


class ReviewSettings(models.Model):
    """
    Модель для хранения и управления настройками автоответов на отзывы
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='review_settings',
        verbose_name='Компания'
    )
    mask = models.TextField(
        verbose_name='Маска для отзыва'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Настройка автоответов на отзывы'
        verbose_name_plural = 'Настройки автоответов на отзывы'

    def __str__(self):
        return f'Настройка отзывов для {self.company.name}'


class Answer(models.Model):
    """
    Модель для хранения ответов на отзывы
    """

    TYPE_CHOICES = [
        (0, 'Ответ создан автоматически'),
        (1, 'Ответ от пользователя')
    ]

    review = models.OneToOneField(
        Review,
        on_delete=models.CASCADE,
        verbose_name='Отзыв',
        related_name='answer'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        null=True,
        blank=True
    )
    body = models.TextField(
        verbose_name='Ответ на отзыв'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Пользователь'
    )
    type = models.CharField(
        max_length=100,
        choices=TYPE_CHOICES,
        verbose_name='Тип ответа'
    )

    class Meta:
        verbose_name = 'Ответ на отзыв'
        verbose_name_plural = 'Ответы на отзывы'

    def __str__(self):
        return f'Ответ на отзыв {self.review.full_name}'


class RateInfo(models.Model):
    first_rate = models.IntegerField(
        verbose_name='Первый тариф'
    )
    second_rate = models.IntegerField(
        verbose_name='Второй тариф'
    )
    third_rate = models.IntegerField(
        verbose_name='Третий тариф'
    )

    class Meta:
        verbose_name = 'Информация о тарифах'
        verbose_name_plural = 'Информации о тарифах'

    def __str__(self):
        return f'Информация {self.id}'
