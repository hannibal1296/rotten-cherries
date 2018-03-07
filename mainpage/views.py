from django.shortcuts import render
from account.models import *


def get_all_dept():
    return Department.objects.all()


def get_all_major():
    return Major.objects.all()


def mainpage(request):
    return render(request, 'mainpage/mainpage.html')
