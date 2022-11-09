import requests
from ..models import TelebotSettings


def send_message_to_admin_telegram_service(message):
    if TelebotSettings.objects.first():
        settings = TelebotSettings.objects.first()
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        api = f'https://api.telegram.org/bot{token}/sendMessage?user_id=-{chat_id}&text={message}'
        try:
            req = requests.post(api, data={
                'chat_id': chat_id,
                'text': message
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print("Ошибка отправки сообщения telegram")
            elif req.status_code == 500:
                print("Ошибка 500")
            else:
                print("Сообщение отправлено")
