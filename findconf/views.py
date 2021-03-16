from django.shortcuts import render
from django.http import HttpResponse
from .alg_to_find import *


def index(request):
    return render(request, 'findconf/index.html')

def test(request):
    return render(request, 'findconf/next_step.html')