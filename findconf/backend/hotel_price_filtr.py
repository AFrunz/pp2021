import findconf.backend.hotel_api as hotel_api

def price_filtr(hotel_price, budget):
    return hotel_price<budget
a = hotel_api.hotel_api("MOW", "2021-04-14", "2021-04-14")
b = a.get_res()
ans = price_filtr(b, 4000)
#True - входит в бюджет, False - нет