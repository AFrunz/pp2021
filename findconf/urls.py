from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('search/', second_step),
    path('search1/', third_step),
]