"""Получение кода города или аэропорта (сделано)
Входные данные: Имя города на русском
Выходные данные: Код города если он был найден, -1 если нет"""
import json
import requests


class get_IATA_code:
    """Класс для получения кода города с помощью города, на вход имя на русском(можно поменять на англ),
    если нет этого города в списке(если это деревня в глуши), то возвращает -1"""
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
        b = json.loads(requests.get(self.__link).text)
        if len(b) > 0:
            self.__code = b[0]['code']
        else:
            self.__code = -1

    def get_res(self):
        """Возврат кода"""
        return self.__code

