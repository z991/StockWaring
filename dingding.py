from dingtalkchatbot.chatbot import DingtalkChatbot


class Ding:

    def __init__(self):
        self.webhook = "你自己钉钉机器人的webhook"

    def send_text(self, message):
        dingding = DingtalkChatbot(self.webhook)
        dingding.send_text(msg=message)
