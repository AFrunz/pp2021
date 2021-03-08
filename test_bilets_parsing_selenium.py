from bs4 import BeautifulSoup as BS
import Selenium_parse


class plane_dict:
    """Информация о самолете"""
    def __init__(self):
        self.company = None
        self.link = None
        self.price = None
        self.transplants = None
        self.port_iz =None
        self.port_v = None
        self.time_iz = None
        self.time_v = None
        self.type = None
        self.bag = None

    def Print_s(self):
        """Вывод переменных"""
        print(self.company, self.link, self.price, self.transplants, self.port_iz, self.time_iz, self.port_v,self.time_v, self.type, self.bag)

class fly_ticket:
    def __init__(self, city_from, city_to, day, month):
        self.city_from = city_from
        self.city_to = city_to
        self.day = day
        self.month = month
        self.__link_up()
        self.__parse()

    def __link_up(self):
        """Модификация ссылки"""
        link = "https://www.svyaznoy.travel/#MOW0203/LED/A1/C0/I0/S0"
        ###
        self.link = link

    def __parse(self):
        a = Selenium_parse.fly_selenium(self.link)
        html = a.get_res()
        self.__get_info(html)

    def get_res(self):
        return self.data

    def __get_info(self, html):
        new_html = BS(html, "html.parser")
        data = new_html.find_all("div", class_="result _ow")
        g_dict = []
        base_link_for_user = 'https://www.svyaznoy.travel/'
        for i in data:
            a = plane_dict()
            # 1. Компания
            s = i.find("span", class_="resline__compname")
            s = s.get_text()
            a.company = s
            # 2. Ссылка
            s = i.find("a", class_="result__link base-button")
            s = s["href"]
            link_for_user = base_link_for_user + s
            a.link = link_for_user
            # 3. Цена
            s = i.find("div", class_="result__price")
            s = s.get_text()
            a.price = s
            # 4. Пересадки
            s = i.find("div", class_="resline__col _time").find("div", class_="resline__transition")
            s = s.get_text()
            a.transplants = s
            # 5. Время из
            s = i.find("div", class_="resline__col _start").find("div", class_="resline__time")
            s = s.get_text()
            a.time_iz = s
            # 6. Время прилета
            s = i.find("div", class_="resline__col _finish").find("div", class_="resline__time")
            s = s.get_text()
            a.time_v = s
            # 7. Порт отлета
            s = i.find("div", class_="resline__col _start").find("div", class_="resline__city").find("span",
                                                                                                     class_="resline__gray")
            if s is None:
                p = i.find("div", class_="resline__col _start").find("span", class_="resline__cityname")
                p = p.get_text()
                a.port_iz = p
            else:
                s = s.get_text()
                a.port_iz = s
            # 8. Порт прилета
            s = i.find("div", class_="resline__col _finish").find("div", class_="resline__city").find("span",
                                                                                                      class_="resline__gray")
            if s is None:
                p = i.find("div", class_="resline__col _finish").find("span", class_="resline__cityname")
                p = p.get_text()
                a.port_v = p
            else:
                s = s.get_text()
                a.port_v = s
            # 9. Тип полета
            s = i.find("div", class_="resline__col _time").find("div", class_="resline__type")
            s = s.get_text()
            a.type = s
            # 10. Багаж
            s = i.find("span", class_="r-bag__info")
            s = s.get_text()
            a.bag = s
            g_dict.append(a)
        self.data = g_dict


b = fly_ticket(1, 1, 1, 1)
a = b.get_res()
for i in a:
    i.Print_s()

