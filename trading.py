import datetime


class Trading:

    def is_start(self, config):
        """
        判断是否为股票交易日(周一到周五，9:30-11:30 13:00-15:00)
        :return:
        """
        now = datetime.datetime.now()
        hour = now.hour
        min = now.minute
        week = now.weekday()

        result = 1
        is_start = config.manual_control()

        if is_start == "ON":
            return 1
        if is_start == "OFF":
            return 0

        if week not in range(1, 6):
            result = 0
        if (hour == 9 or hour == 11) and min in range(0, 30):
            result = 0
        if hour in range(0, 9) or hour in range(15, 24) or hour == 0:
            result = 0

        if (week not in range(1, 6)) and ((hour == 9 or hour == 11) and min in (0, 31)):
            result = 0
        if hour in range(0, 9) or hour in range(15, 24) or hour == 0:
            result = 0
        return result
