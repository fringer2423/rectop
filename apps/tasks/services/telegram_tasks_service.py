import requests

from celery import shared_task
from datetime import datetime


@shared_task(queue='telegram_push')
def send_message_task(chat_id, token, message):
    """Отправляет сообщение в telegram"""
    api = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=-{chat_id}&text={message}'

    req = requests.post(api, data={
        'chat_id': chat_id,
        'text': message
    })
