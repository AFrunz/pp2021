from django.shortcuts import render, redirect
from django.http import HttpResponse
from .step1 import *
from .backend.train_pars import train_parse
from .models import feedback, country_info, city_info
import json


# from .forms import IndexForm


def index(request):
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
        print(d)
        conf = get_res(d["country"], d["city"], d["theme"], d["keywords"], d["money_do"],
                       d["date_s"], d["date_f"])
        return render(request, 'findconf/second_step.html', context={"conf": conf})
    # {"conf": conf}
    if request.method == "POST":
        country = request.POST.get("country")
        print(country)
    return render(request, 'findconf/second_step.html')


def third_step(request):
    a = train_parse("Москва", "Санкт-Петербург", "24апреля2021г", "26апреля2021г")
    print(a.get_aver())
    return render(request, 'findconf/third_step.html')


def zero_step(request):
    print(request.POST.get("select_country"))
    return redirect(second_step)


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
        print(i.city_name)
    return HttpResponse(str(l))
