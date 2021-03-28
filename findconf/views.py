from django.shortcuts import render, redirect
from django.http import HttpResponse
from .step1 import *
from .backend.train_pars import train_parse
import json


def index(request):
    return render(request, 'findconf/index.html')


def second_step(request):
    get_res()
    if request.method == "POST":
        country = request.POST.get("country")
        print(country)
    return render(request, 'findconf/second_step.html')


def third_step(request):
    a = train_parse("Москва", "Санкт-Петербург", "24апреля2021г", "26апреля2021г")
    print(a.get_aver())
    return render(request, 'findconf/third_step.html')


