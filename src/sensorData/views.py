import datetime

from django.shortcuts import render, redirect

from sensorData.models import Data


def home(request, date=datetime.date.today()):
    datas = Data.objects.filter(created__contains=date)
    return render(request, 'home.html', {'datas': datas})
