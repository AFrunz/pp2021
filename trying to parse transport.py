import requests
from bs4 import BeautifulSoup as BS
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
                         'Chrome/86.0.4240.111 Safari/537.36', 'accept': '*/*'
           }
class plane_dict:
    """Информация о самолете"""
    def __init__(self):
        self.number = None
        #self.link = None - не получилось, проблема с парсингом
        self.port_iz = None
        self.port_v = None
        self.time_iz = None
        self.time_v = None
        self.rating = None
        self.price =None
        self.type = None
    def Print_s(self):
        print(self.number, self.port_iz, self.time_iz, self.port_v,self.time_v, self.rating, self.type)

class avia_parse():
    link = "https://www.kayak.ru/flights/MOW-LED/2021-03-02?sort=bestflight_a"
    def __init__(self, city_from, city_to, day, month):
        self.city_from = city_from
        self.city_to = city_to
        self.day = day
        self.month = month
        self.__parse()

    def getRes(self):
        """Получение результатов парсинга"""
        return self.result

    def __linkUpdate(self):
        """Модификация ссылки с учетом вводных данных"""
        pass

    def __parse(self):
        """Основа парсера"""
        Html = self.__getHTML()
        self.result = self.__getInf(Html)

    def __getHTML(self):
        """Получение HTML кода"""
        link = self.link
        return requests.get(link, headers=HEADERS)

    def __getInf(self, html):
        """Получение необходимой информации"""
        new_html = BS(html.text, "html.parser")        array_of_inf = []
        data = new_html.find_all("div", class_="resultWrapper")
        # for i in data:
        #     a = plane_dict()
        #     """Заполняем словарь ценами"""
        #     s = i.find("div", class_ = "Common-Booking-MultiBookProvider featured-provider cheapest multi-row Theme-featured-large").find("span", class_="price-text")
        #     s = str(s.get_text())
        #     a.price =s[:-2].strip()
        #     """Заполняет компаниями"""
        #     s = i.find("div", class_="yoFb-carrier-text")
        #     s = s.get_text()
        #     a.number = str(s).strip()
        #     """Заполняет аэропортами"""
        #     s = i.find_all("span", class_ = "airport-name")
        #     fn = str(s[0])
        #     fn = fn.replace("\n", "")
        #     fn = fn[1:-1]
        #     a.port_iz = fn
        #     ln = str(s[1])
        #     ln = ln.replace("\n", "")
        #     ln = ln[1:-1]
        #     a.port_v = ln
        #     """Время вылета"""
        #     fti = i.find_all("span", class_="depart-time base-time")
        #     fti = fti.get_text()
        #     a.time_iz = fti.split()
        #     """Время прилета"""
        #     sti = i.find_all("span", class_="arrival-time base-time")
        #     sti = sti.get_text()
        #     a.time_v = sti.split()
        #     """Рейтинг"""
        #     r = i.find("span", class_="_ial _idj _iaj")
        #     r = r.get_txt()
        #     a.rating = r.split()
        #     """Тип полета"""
        #     t = i.find("div", class_="yoFb-cabin-class js-farename")
        #     t = t.get_text()
        #     a.type = t.split()
        #     array_of_inf.append(a)
        # return array_of_inf
a = avia_parse(12,12,12,12)
c = a.getRes()
# for i in c:
#     print(i.price, i.number, i.port_iz, i.port_v, i.time_iz, i.time_v, i.rating, i.type)
