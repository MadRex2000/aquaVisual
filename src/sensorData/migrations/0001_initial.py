# Generated by Django 3.2.9 on 2021-11-19 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名稱')),
                ('location', models.CharField(max_length=100, verbose_name='地點')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(verbose_name='溫度')),
                ('ph', models.FloatField(verbose_name='pH值')),
                ('tds', models.FloatField(verbose_name='總溶解量')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='sensorData.sensor', verbose_name='感測器')),
            ],
        ),
    ]