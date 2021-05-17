"""Получение данных цен на отели (сделано)
Входные данные: Город, дата заезда и дата выезда
Выходные данные: Средняя цена на отели"""

import requests
import json
from findconf.models import hotel_info
import datetime


def strtodate(date):
    if date == '':
        return -1
    day = ''
    month = ''
    d = {"янв": "01", "фев": "02", "мар": "03", "апр": "04", "мая": "05", "июн": "06",
         "июл": "07", "ав": "08", "сен": "09", "окт": "10", "ноя": "11", "дек": "12"}
    for j in d:
        pos = date.find(j)
        if pos != -1:
            if pos == 1:
                day = '0' + date[:pos]
            else:
                day = date[:pos]
            month = d[j]
            break
    if day != '':
        new_date = date[-5:-1] + '-' + month + '-' + day
        return new_date
    return date


def date_str_to_cal(f_date, pon):
    date_year = int(f_date[0:4])
    date_month = int(f_date[5:7])
    date_day = int(f_date[8:10])
    date = datetime.date(date_year, date_month, date_day)
    p_day = datetime.timedelta(days=1)
    tomorrow_date = date + p_day
    yesterday_date = date - p_day
    if pon == 1:
        str_t = str(tomorrow_date)
        return str_t
    elif pon == -1:
        str_y = str(yesterday_date)
        return str_y
    else:
        return -1


class hotel_api:

    def __init__(self, city, start_date, finish_date):
        self.city = city
        self.start_date = date_str_to_cal(strtodate(start_date), -1)
        self.finish_date = date_str_to_cal(strtodate(finish_date), 1)
        self.__getInfo()
        self.__table_p()

    def __linkup(self):
        link_city = "location=" + self.city
        link_currency = "&currency=rub"
        link_start_date = "&checkIn=" + self.start_date
        link_finish_date = "&checkOut=" + self.finish_date
        link_limit = "&limit=1000"
        self.link = "http://engine.hotellook.com/api/v2/cache.json?" + link_city + link_currency + link_start_date + \
                    link_finish_date + link_limit

    def __getData(self):
        self.__linkup()
        data = requests.get(self.link)
        return data.text

    def __getInfo(self):
        data = self.__getData()
        info = json.loads(data)
        prices = []
        for i in range(0, len(info)):
            prices.append(info[i]["priceAvg"])
        prices = sorted(prices)
        if len(prices) > 0:
            sr = len(prices) // 2
            res = prices[sr]
            self.res = res
        else:
            self.res = -1

    def get_res(self):
        return self.res

    def __table_p(self):
        a = hotel_info(city=self.city, date_start=self.start_date, date_finish=self.finish_date,
                       price=self.res)
        a.save()
