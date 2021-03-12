"""Получает информацию о ценах на авиабилеты ( модификатор ссылки вроде есть, сделано )"""
"""В разное время билеты стоят по разному, а тут мы считаем среднее билетов за все время"""
"""Исправил, но маловато самолетов он находит(1 обычно, 0 - реже)"""

import requests
import json

class fly_price_info:
    """Класс возвращает среднюю цену по перелетам"""
    def __init__(self, origin, destination, date_start, date_finish):
        self.origin = origin
        self.destination = destination
        self.date_start = date_start
        self.date_finish = date_finish
        self.__link_up()
        self.__get()
        self.__analysys()

    def __link_up(self):
        """Модификация ссылки"""
        token = "&token=7051a5c613492481369c11039ff6d599"
        link = "http://api.travelpayouts.com/v2/prices/latest?currency=rub&page=1&limit=1000&one_way=false&show_to_affiliates=true&sorting=price"
        link += '&origin=' + str(self.origin) + '&destination=' + str(self.destination) + '&' + token
        self.link = link


    def __filter(self, data):
        new_data = []
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
        data = self.__filter(data)
        for i in data:
            summa += i["value"]
            k += 1
        if k != 0:
            summa = summa // k
        self.sr = summa

    def get_res(self):
        return self.sr


b = fly_price_info("MOW", "PEE", "2021-03-14", "2021-03-19")
c = b.get_res()
