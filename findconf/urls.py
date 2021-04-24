from django.urls import path
from django.views.generic import RedirectView

from .views import *
urlpatterns = [
    path('', index),
    path('search/', second_step),
    path('search1/', third_step),
    path('zero/', zero_step),
    path('feedback/', Feedback),
    path(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
    path(r'^bootstrap.min.css$', RedirectView.as_view(url='/static/bootstrap.min.css', permanent=True)),
    path('about_us/', About_us),
    path('get_city/', Get_city_),
]