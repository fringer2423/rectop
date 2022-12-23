import requests
from django.db.models import QuerySet
from requests import Response

from ..models import TelebotSettings


def send_message_to_admin_telegram_service(message: str) -> None:
    """Функция отправки сообщения в telegram"""
    if TelebotSettings.objects.first():
        settings: QuerySet[TelebotSettings] = TelebotSettings.objects.first()
        token: str = str(settings.tg_token)
        chat_id: str = str(settings.tg_chat)
        api: str = f'https://api.telegram.org/bot{token}/sendMessage?user_id=-{chat_id}&text={message}'
        try:
            req: Response = requests.post(api, data={
                'chat_id': chat_id,
                'text': message
            })
        except Exception as e:
            print(e)
        finally:
            if req.status_code != 200:
                print("Ошибка отправки сообщения telegram")
            elif req.status_code == 500:
                print("Ошибка 500")
            else:
                print("Сообщение отправлено")
