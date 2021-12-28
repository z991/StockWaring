import configparser
import json


class ConfigStock:
    """
    获取股票配置信息
    """
    def __init__(self):
        self.conf_main = configparser.ConfigParser()
        self.conf = self.conf_main.read("config.ini")

    def get_stock_json(self):
        """
        获取要监控的股票信息
        :return:
        """
        stock_json = self.conf_main.get('stock_config', 'stock_list')
        return json.loads(stock_json)

    def manual_control(self):
        """
        判断是否开始监控或者停止监控
        :return:
        """
        task_status = self.conf_main.get('stock_config', 'task_status')
        return task_status

