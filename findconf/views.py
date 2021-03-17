from django.shortcuts import render
from django.http import HttpResponse
from .alg_to_find import *


def index(request):
    return render(request, 'findconf/index.html')

def second_step(request):
    return render(request, 'findconf/second_step.html')

def third_step(request):
    return render(request, 'findconf/third_step.html')