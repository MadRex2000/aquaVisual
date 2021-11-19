from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='名稱')
    location = models.CharField(max_length=100, verbose_name='地點')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Data(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='data', on_delete=models.CASCADE, verbose_name='感測器')
    temp = models.FloatField(verbose_name='溫度')
    ph = models.FloatField(verbose_name='pH值')
    tds = models.FloatField(verbose_name='總溶解量')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
