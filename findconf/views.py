from django.shortcuts import render, redirect
from django.http import HttpResponse
from .step1 import *
from .backend.train_pars import train_parse
import json


def index(request):
    return render(request, 'findconf/index.html')


def second_step(request):
    link = '/search/?country=&city=&theme=&keywords=&money_ot=&money_do=&date_s=&date_f='
    if request.method == "POST":
        country = request.POST.get("country")
        city = request.POST.get("city")
        theme = request.POST.get("theme")
        keywords = request.POST.get("keywords")
        money_ot = request.POST.get("money_ot")
        money_do = request.POST.get("money_do")
        date_s = request.POST.get("date_s")
        date_f = request.POST.get("date_f")
        conf = get_res(country, city, theme, keywords, money_ot, money_do, date_s, date_f)
        return render(request, 'findconf/second_step.html', {"conf": conf})
    if request.method == "POST":
        country = request.POST.get("country")
        print(country)
    return render(request, 'findconf/second_step.html')


def third_step(request):
    a = train_parse("Москва", "Санкт-Петербург", "24апреля2021г", "26апреля2021г")
    print(a.get_aver())
    return render(request, 'findconf/third_step.html')


