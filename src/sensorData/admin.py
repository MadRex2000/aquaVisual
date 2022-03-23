from django.contrib import admin
from .models import Sensor, Data, ClassData

admin.site.register(Sensor)
admin.site.register(Data)
admin.site.register(ClassData)
