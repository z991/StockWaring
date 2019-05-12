from dingtalkchatbot.chatbot import DingtalkChatbot


class Ding:

    def __init__(self, webhook):
        self.webhook = webhook

    def send(self, message):
        xiaoding = DingtalkChatbot(self.webhook)
        xiaoding.send_text(msg=message, is_at_all=True)
