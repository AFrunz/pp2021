from django.shortcuts import render, redirect
from django.http import HttpResponse
from .step1 import *
from .backend.train_pars import train_parse
# from .backend.sf import dr
# from .backend.citiesname import g
from .models import feedback, country_info, city_info
import json


# from .forms import IndexForm


def index(request):
    table_clear()
    return render(request, 'findconf/index.html')


def second_step(request):
    link = '/search/?country=&city=&theme=&keywords=&money_ot=&money_do=&date_s=&date_f='
    # Через строку - метод гет, через форму - метод пост.
    if request.method == "GET":
        d = {}
        d["country"] = request.GET.get("select_country")
        d["city"] = request.GET.get("select_city")
        d["theme"] = request.GET.get("select_theme")
        d["keywords"] = request.GET.get("keywords")
        d["money_do"] = request.GET.get("budget")
        d["date_s"] = request.GET.get("date_start")
        d["date_f"] = request.GET.get("date_finish")
        conf = get_res(d["city"], d["theme"], d["keywords"], d["money_do"],
                       d["date_s"], d["date_f"])
        for i in conf:
            if type(i["train"]) != dict:
                if i["train"] < 0:
                    i["medium"] = -1
                elif i["train"] == 0:
                    if i["plane"] is not None and i["plane"] != -2:
                        if i["hotel"] is not None:
                            i["medium"] = i["plane"] + i["hotel"]
                        else:
                            i["medium"] = -1
                    else:
                        i["medium"] = -1
            else:
                if i["plane"] is not None:
                    i["medium"] = min(i["plane"], i["train"]["Купе"]) + i["hotel"]
                elif i["hotel"] is not None:
                    i["medium"] = i["train"]["Купе"] + i["hotel"]
                else:
                    i["medium"] = -1
        conf1 = []
        if d["money_do"] != "":
            for i in conf:
                if i["medium"] <= float(d["money_do"]):
                    conf1.append(i)
            return render(request, 'findconf/second_step.html', context={"conf": conf1, "inf": d})
        return render(request, 'findconf/second_step.html', context={"conf": conf, "inf": d})


# def third_step(request):
#     a = train_parse("Москва", "Санкт-Петербург", "24апреля2021г", "26апреля2021г")
#     print(a.get_aver())
#     return render(request, 'findconf/third_step.html')
#
#
# def zero_step(request):
#     return redirect(second_step)

def half_step(request):
    return render(request, 'findconf/csrf.html')


def Feedback(request):
    if request.method == "POST":
        s = request.POST["Feedbackinput"]
        print(s, type(s))
        base = feedback(info=s)
        base.save()
        return redirect(index)
    else:
        return render(request, "findconf/FeedBack.html")


def About_us(request):
    return render(request, "findconf/about_us.html")


def Get_city_(request):
    s = request.GET["Id"]
    if s == '':
        return HttpResponse('')
    base = city_info.objects.filter(city_country_id=s)
    l = []
    for i in base:
        l.append(i.city_id)
    return HttpResponse(str(l))
