from selenium import webdriver
import time
from bs4 import BeautifulSoup as BS
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
        print(self.company, self.link, self.price, self.transplants, self.port_iz, self.time_iz, self.port_v,self.time_v, self.type, self.bag)
link = "https://www.svyaznoy.travel/#MOW0203/LED/A1/C0/I0/S0"
base_link_for_user = "https://www.svyaznoy.travel/"
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)
browser.get(link)
time.sleep(20)
html = browser.page_source
new_html = BS(html, "html.parser")
data = new_html.find_all("div", class_="result _ow")
for i in data:
    a = plane_dict()
    # 1. Компания
    s = i.find("span", class_="resline__compname")
    s = s.get_text()
    print(s, end = ' ')
    a.company = s
    # 2. Ссылка
    s = i.find("a", class_="result__link base-button")
    s = s["href"]
    link_for_user = base_link_for_user + s
    a.link = link_for_user
    print(link_for_user, end=" ")
    # 3. Цена
    s = i.find("div", class_ = "result__price")
    s = s.get_text()
    print(s, end=" ")
    a.price = s
    # 4. Пересадки
    s = i.find("div", class_="resline__col _time").find("div", class_="resline__transition")
    s = s.get_text()
    print(s, end = " ")
    a.transplants = s
    # 5. Время из
    s = i.find("div", class_= "resline__col _start").find("div", class_="resline__time")
    s = s.get_text()
    print(s, end=" ")
    a.time_iz = s
    # 6. Время прилета
    s = i.find("div", class_= "resline__col _finish").find("div", class_="resline__time")
    s = s.get_text()
    print(s, end = " ")
    a.time_v = s
    # 7. Порт отлета
    s = i.find("div", class_ = "resline__col _start").find("div", class_ = "resline__city").find("span", class_="resline__gray")
    if s is None:
        p = i.find("div", class_ = "resline__col _start").find("span", class_ = "resline__cityname")
        p = p.get_text()
        a.port_iz = p
        print(p, end =" ")
    else:
        s = s.get_text()
        a.port_iz = s
        print(s, end=" ")
    # 8. Порт прилета
    s = i.find("div", class_ = "resline__col _finish").find("div", class_ = "resline__city").find("span", class_="resline__gray")
    if s is None:
        p = i.find("div", class_ = "resline__col _finish").find("span", class_ = "resline__cityname")
        p = p.get_text()
        a.port_v = p
        print(p, end =" ")
    else:
        s = s.get_text()
        a.port_v = s
        print(s, end=" ")
    # 9. Тип полета
    s = i.find("div", class_="resline__col _time").find("div", class_="resline__type")
    s = s.get_text()
    a.type = s
    print(s, end=" ")
    # 10. Багаж
    s = i.find("span", class_ = "r-bag__info")
    s = s.get_text()
    a.bag = s
    print(s)
