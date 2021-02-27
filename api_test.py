from selenium import webdriver
import time
class fly_selenium:

    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options)
        self.__link_update()
        html = self.__get_html()

    def get_res(self):
        return self.html

    def __link_update(self):
        self.link = "https://www.kupibilet.ru/search/Y10002MARMOWLED"



    def __get_html(self):
        self.browser.get(self.link)
        time.sleep(10)
        self.html = self.browser.page_source



    # def log(init, browser):
    #     browser.get('https://lolz.guru/login/')
    #     time.sleep(3)
    #     email = browser.find_element_by_id('ctrl_pageLogin_login')
    #     password = browser.find_element_by_id('ctrl_pageLogin_password')
    #     email.send_keys('frunzea2@yandex.ru')
    #     password.send_keys('alex2042')
    #     login = browser.find_element_by_class_name("large")
    #     login.click()
    #     return browser


    # def get_l(init, link, browser):
    #     browser.get(link)
    #     return browser.page_source

a = fly_selenium()
print(a.get_res())