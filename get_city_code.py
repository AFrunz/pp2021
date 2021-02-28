# Доделано
import requests
import json


class get_IATA_code:
    """Класс для получения кода города с помощью города, на вход имя на русском(можно поменять на англ"""
    def __init__(self, name):
        self.__name = name
        self.__link_update()
        self.__get_code()

    def __link_update(self):
        """Модификация ссылки"""
        link = "http://autocomplete.travelpayouts.com/places2?term=&locale=ru&types[]=city"
        self.__link = link[:link.find("term")+5] + str(self.__name) + link[link.find("&"):]

    def __get_code(self):
        """Получение кода"""
        b = json.loads(requests.get(self.__link).text)[0]
        self.__code = b['code']

    def get_res(self):
        """Возврат кода"""
        return self.__code


a = get_IATA_code("Москва")
print(a.get_res())