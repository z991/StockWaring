from dingtalkchatbot.chatbot import DingtalkChatbot


class Ding:

    def __init__(self):
        self.webhook = 'https://oapi.dingtalk.com/robot/send?access_token=6e2ce71ae16374dd4edbdf6d1b12a605599e34da3e1ce92c98199def3eadcea2'

    def send(self, message):
        xiaoding = DingtalkChatbot(self.webhook)
        xiaoding.send_text(msg=message, is_at_all=True)
