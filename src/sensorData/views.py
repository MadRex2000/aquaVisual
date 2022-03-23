import datetime

from django.shortcuts import render, redirect

from sensorData.models import Data, ClassData


def home(request, date=datetime.date.today(), data_type='iot'):
    if data_type == 'iot':
        datas = ClassData.objects.filter(created__contains=date).order_by('id')
        return render(request, 'iot.html', {'datas': datas})
    else:
        datas = Data.objects.filter(created__contains=date).order_by('id')
        return render(request, 'home.html', {'datas': datas})
