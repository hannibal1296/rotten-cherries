from django.urls import path
from . import views
from django.shortcuts import redirect


def to_main(request):
    redirect('')


urlpatterns = [
    path('', views.mainpage, name='mainpage'),
]
