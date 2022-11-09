from django.db import models


class TelebotSettings(models.Model):
    """Модель для настройки telegram бота"""

    class Meta:
        verbose_name = 'Настройка бота'
        verbose_name_plural = 'Настройки ботов'

    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Chat id')
    is_admin_bot = models.BooleanField(default=False, verbose_name='Is admin bot')

    def __str__(self):
        message = f'Бот {self.tg_token}'
        if self.is_admin_bot:
            message = 'Admin ' + message
        return message
