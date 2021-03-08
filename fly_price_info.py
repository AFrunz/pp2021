import requests
import json

class fly_price_info:
    """Класс возвращает среднюю цену по перелетам"""
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.__link_up()
        self.__get()
        self.__analysys()

    def __link_up(self):
        """Модификация ссылки"""
        token = "&token=7051a5c613492481369c11039ff6d599"
        link = "http://api.travelpayouts.com/v2/prices/latest?currency=rub&page=1&limit=1000&one_way=true&show_to_affiliates=true&sorting=price"
        link += '&origin=' + str(self.origin) + '&destination=' + str(self.destination) + '&' + token
        self.link = link

    def __get(self):
        """Получение результатов запроса"""
        a = requests.get(self.link).text
        self.info = json.loads(a)

    def __analysys(self):
        data = self.info["data"]
        sum = 0
        k = 0
        sr = len(data) // 2
        print(data[sr]["value"])
        for i in data:
            sum += i["value"]
            k += 1
        if k != 0:
            sum = sum // k
        self.sr = sum
        print(sum)
    def get_res(self):
        return self.sr


b = fly_price_info("MOW", "LED")
c = b.get_res()
