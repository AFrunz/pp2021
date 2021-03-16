# 1) Ввод данных (на потом, ввод будет с сайта)
# 2) Поиск конференций по теме
# 3) Применение фильтра для дат
# 4) Составления для каждой конференции словаря:
# Конференция, город, цена на авиабилет, цена на поезд, цена на проживание, код города этой конференции(можно
# расширять словарь, содержащий инфу о конференциях
# 5) Отсеять конференции, не подходящие по бюджету
# 6) Получить массив словарей с необходимой информацие
# 7) Далее зависит от интерфейса, пока оставляем


from findconf.backend import get_city_code, conf_pars, train_pars, fly_price_info, hotel_api as h
import time



def date_filtr(data_p_s, data_p_e, s_conf):
    right_dates = []
    data_p_s = h.strtodate(data_p_s)
    # "2021-03-21    2021-03-13
    data_p_e = h.strtodate(data_p_e)
    for i in s_conf:
        date_s = h.strtodate(i.date_start)
        date_e = h.strtodate(i.date_end)
        if data_p_s < date_s < data_p_e and data_p_s < date_e < data_p_e:
            right_dates.append(i)
    return right_dates
# 1. Пользователь выбирает тематику
# Допустим пользователь выбрал тематикой математику. Также допустим, что человек живет в Москве.
def get_res():
    t1 = time.time()
    tema = "Математика"
    home_city = "Москва"
    data_p_s = "1апреля2021г"
    data_p_e = "29июня2021г"


# 2. Поиск всех конференций по тематике

    s_conf = conf_pars.Conf_parser(1, 1, 1, 1)
    s_conf = s_conf.getRes()
    s_conf = date_filtr(data_p_s, data_p_e, s_conf)
    home_city_code = get_city_code.get_IATA_code(home_city)
    home_city_code = home_city_code.get_res()

# 3.2 Для каждой конференции считается цена на билет на поезд/цена на билет на самолет/проживание

    for j in s_conf:
        city_code = get_city_code.get_IATA_code(j.city)
        city_code = city_code.get_res()
        j.code = city_code
        if j.code == -1:
            j.train = -1
            j.plane = -1
            j.hotel = -1
        elif j.code == home_city_code:
            j.train = 0
            j.plane = 0
            j.hotel = 0
        else:
            #Достаем цену
            train_price = train_pars.train_parse(home_city, j.city, j.date_start, j.date_end)
            train_p = train_price.get_average()
            j.train = train_p
            #j.train = train_price
            plane_price = fly_price_info.fly_price_info(home_city_code, j.code, j.date_start, j.date_end)
            plane_p = plane_price.get_res()
            j.plane = plane_p
            hotel_price = h.hotel_api(j.code, j.date_start, j.date_end)
            hotel_p = hotel_price.get_res()
            j.hotel = hotel_p
    for i in s_conf:
        i.Print_s()
    t2 = time.time()
    return s_conf

# 4 Выводятся результаты
# for i in data:
#     print("Конференция будет в городе " + i["city"], end=',')
#     if i["city"] == home_city:
#         print("вы живете в этом городе")
#     elif i["code"] == -1:
#         print("средняя цена не найдена")
#     else:
#         if i["plane"] != -1:
#             print("средняя цена на самолет = " + str(i["plane"]), end=',')
#         else:
#             print("средняя цена на самолет не найдена", end=',')
#         if i["hotel"] != -1:
#             print("средняя цена на отель = " + str(i["hotel"]))
#         else:
#             print("средняя цена на отель не найдена")
