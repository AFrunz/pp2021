#1. Пользователь выбирает тематику
    #Допустим пользователь выбрал тематикой математику. Также допустим, что человек живет в Москве.
tema = "Математика"
home_city = "Москва"
#2. Поиск всех конференций по тематике
import conf_pars
s_conf = conf_pars.Conf_parser(1, 1, 1, 1)
s_conf = s_conf.getRes()
cities = []
dates_conf_start = []
dates_conf_finish = []
for i in s_conf:
    cities.append(i.city)
    dates_conf_start.append("2021-03-25")#Когда преобразуем дату - поменяем
    dates_conf_finish.append("2021-03-27")#Когда преобразуем дату - поменяем
#3.1 Получение самолетного кода для всех городов конференций
import get_city_code
home_city_code = get_city_code.get_IATA_code(home_city)
home_city_code = home_city_code.get_res()
cities_codes = []
for i in cities:
    if i == "Белово":
        cities_codes.append(-1)
    else:
        city_code = get_city_code.get_IATA_code(i)
        city_code = city_code.get_res()
        cities_codes.append(city_code)
sr_samolet = []
sr_otel = []
import fly_price_info
for i in cities_codes:
    if i == -1:
        sr_samolet.append(-1)
    elif i == home_city_code:
        sr_samolet.append(0)
    else:
        samolet_price = fly_price_info.fly_price_info(home_city_code,i)
        samolet_price = samolet_price.get_res()
        sr_samolet.append(samolet_price)
import hotel_api
for i in range(0, len(cities_codes)):
    if cities_codes[i] == -1:
        sr_otel.append(-1)
    elif cities_codes[i] == home_city_code:
        sr_otel.append(0)
    else:
        otel_price = hotel_api.hotel_api(cities_codes[i], dates_conf_start[i], dates_conf_finish[i])
        otel_price = otel_price.get_res()
        sr_otel.append(otel_price)
#3.2 Для каждой конференции считается цена на билет на поезд/цена на билет на самолет/проживание

#4 Выводятся результаты
for i in range(0, len(cities)):
    print("Конференция будет в городе " + cities[i], end = ',')
    if cities[i] == home_city:
        print("вы живете в этом городе")
    elif cities_codes[i] == -1:
        print("средняя цена не найдена")
    else:
        if sr_samolet[i]!= -1:
            print("средняя цена на самолет =" + str(sr_samolet[i]), end = ',')
        else:
            print("средняя цена на самолет не найдена", end = ',')
        if sr_otel[i]!= -1:
            print("средняя цена на отель =" + str(sr_otel[i]))
        else:
            print("средняя цена на отель не найдена")