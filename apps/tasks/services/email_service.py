import logging

from django.core.mail import send_mail
from django.conf import settings


def send_email_service(subject, body, email):
    logger = logging.getLogger('celery')
    subject = "Администратор Rectop"
    body = body + "\n --\n C уважением,\n Rectop \n +7 (999) 999-99-99 \n admin@rectop.ru "
    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, [email], fail_silently=False)
    except Exception as err:
        logger.error(f'Email не отправлен {err}')
