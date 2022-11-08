import logging
import requests
from copy import copy
from datetime import datetime
from django.conf import settings
from django.utils.module_loading import import_string

from apps.tasks.services.telegram_tasks_service import send_message_task

token = settings.TELEGRAM_LOGGING_TOKEN
chat = settings.TELEGRAM_LOGGING_CHAT
emit_on_debug = getattr(settings, 'TELEGRAM_LOGGING_EMIT_ON_DEBUG', False)


class PseudoFile:
    def __init__(self, content, name):
        self.name = name
        self.content = content

    def read(self):
        return self.content


class TelegramHandler(logging.Handler):
    # noinspection PyUnusedLocal
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.include_html = True
        self.reporter_class = import_string('django.views.debug.ExceptionReporter')

    def emit(self, record):
        if settings.DEBUG and not emit_on_debug:
            return
        # noinspection PyBroadException
        try:
            # noinspection PyUnresolvedReferences
            request = record.request
        except Exception:
            request = None

        no_exc_record = copy(record)
        no_exc_record.exc_info = None
        no_exc_record.exc_text = None

        if record.exc_info:
            exc_info = record.exc_info
        else:
            exc_info = (None, record.getMessage(), None)

        message = record.getMessage()
        print(record.getMessage())
        self.send_message(message)

    def send_message(self, message):
        message = f'{datetime.now().strftime("%Y%m%d%H%M%S")}.{logging.getLevelName(self.level)} - {message}'
        send_message_task.delay(chat_id=chat, token=token, message=message)
