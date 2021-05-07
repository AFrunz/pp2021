from findconf.models import city_info
def dr():
    a = city_info
    f = city_info.objects.all()
    html = ""
    for i in f:
        html += f"<option value=\"{str(i.city_id)}\" hidden>{i.city_name}</option>\n"
    r = open("MyHtml.txt", "w")
    r.write(html)
    r.close()