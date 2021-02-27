from selenium import webdriver
import time


def get_opt():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    return browser


def log(browser):
    browser.get('https://lolz.guru/login/')
    time.sleep(3)
    email = browser.find_element_by_id('ctrl_pageLogin_login')
    password = browser.find_element_by_id('ctrl_pageLogin_password')
    email.send_keys('frunzea2@yandex.ru')
    password.send_keys('alex2042')
    login = browser.find_element_by_class_name("large")
    login.click()
    return browser


def get_l(link, browser):
    browser.get(link)
    return browser.page_source