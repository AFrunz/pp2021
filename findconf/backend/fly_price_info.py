"""Получает информацию о ценах на авиабилеты
Входные данные: Город отправления, город прибытия, дата отправления, дата прибытия
Выходные данные: Средняя цена если самолеты есть, 0 если самолетов нет"""

import requests
import json
from findconf.backend.hotel_api import strtodate
from findconf.models import avia_info
from findconf.backend.hotel_api import date_str_to_cal


class fly_price_info:
    """Класс возвращает среднюю цену по перелетам"""
    def __init__(self, origin, destination, date_start, date_finish):
        self.origin = origin
        self.destination = destination
        self.date_start = date_str_to_cal(strtodate(date_start), -1)
        self.date_finish = date_str_to_cal(strtodate(date_finish), 1)
        self.__link_up()
        self.__get()
        self.__analysys()

    def __link_up(self):
        """Модификация ссылки"""
        token = "&token=7051a5c613492481369c11039ff6d599"
        link = "http://api.travelpayouts.com/v2/prices/latest?currency=rub&page=1&limit=" \
               "1000&one_way=false&show_to_affiliates=true&sorting=price"
        link += '&origin=' + str(self.origin) + '&destination=' + str(self.destination) + '&' + token
        self.link = link

    def __filter(self, data):
        new_data = []
        if data is None:
            return
        for i in data:
            if i["depart_date"] == self.date_start and i["return_date"] == self.date_finish:
                new_data.append(i)
        return new_data

    def __get(self):
        """Получение результатов запроса"""
        a = requests.get(self.link).text
        self.info = json.loads(a)

    def __analysys(self):
        data = self.info["data"]
        summa = 0
        k = 0
        new_data = self.__filter(data)
        if len(new_data) > 0:
            data = new_data
            for i in data:
                summa += i["value"]
                k += 1
            if k != 0:
                summa = summa // k
            self.sr = summa
            self.__table_p()
        else:
            for i in data:
                summa += i["value"]
                k += 1
            if k != 0:
                summa = summa // k
            self.sr = str(summa)

    def get_res(self):
        return self.sr

    def __table_p(self):
        a = avia_info(city_iz=self.origin, city_v=self.destination, date_start=self.date_start,
                      date_finish=self.date_finish, price=self.sr)
        a.save()
