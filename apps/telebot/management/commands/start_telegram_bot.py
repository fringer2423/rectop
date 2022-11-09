import datetime

from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot

bot = TeleBot(settings.TELEGRAM_BOT_TOKEN, threaded=False)


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    @bot.message_handler(commands=["start"])
    def start(message, res=False):
        date = message.date + 10800
        print(f"{datetime.datetime.utcfromtimestamp(date)} /start {message.from_user.first_name}")
        bot.send_message(message.chat.id, 'Я на связи. Напиши мне что-нибудь )')

    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        date = message.date + 10800
        print(f"{datetime.datetime.utcfromtimestamp(date)} send{message.from_user.first_name}")
        bot.send_message(message.chat.id,
                         'Я пока не работаю, но очень скоро начну буду помогать вам с отзывами, ' + message.from_user.first_name + '!')

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()
