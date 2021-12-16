import time

from dingtalkchatbot.chatbot import DingtalkChatbot


class Ding:

    def __init__(self):
        self.webhook = "你自己的钉钉机器人webhook"

    def send(self, message):
        xiaoding = DingtalkChatbot(self.webhook)
        xiaoding.send_text(msg=message)
        time.sleep(2)

