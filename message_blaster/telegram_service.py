from telegram import Bot

class TelegramService:
    def __init__(self, token):
        self.bot = Bot(token)

    def send_message(self, chat_id, text):
        self.bot.send_message(chat_id=chat_id, text=text)