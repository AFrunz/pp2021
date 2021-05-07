#from findconf.models import country_info, city_info
countries = ["Азербайджан", "Армения", "Беларусь","Грузия", "Казахстан", "Литва", "Молдова", "Польша", "Россия", "Сербия", "Узбекистан", "Украина"]
id_country = 1
id_city = 1
for i in countries:
#    p = country_info()
#    q = city_info()
#    p.country_name = i
#    p.country_id = id_country
#    p.save()
    file = open(i+".txt", "r", encoding="utf-8")
    text = file.read()
    text = text + ', '
    while len(text)>0:
        zap = text.find(",")
        c_name = text[:zap]
        #q.city_name = c_name
        #q.city_id = id_city
        #q.city_country_id = id_country
        #q.save()
        text = text[zap:]
        print(c_name, end = " ")
        print(id_city, end = " ")
        print(id_country)
        id_city+=1
        text = text[2:]
    id_country+=1