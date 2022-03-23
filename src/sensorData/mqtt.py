from threading import Thread
import time
import json

from django.conf import settings
import paho.mqtt.client as mqtt

from sensorData.models import ClassData, Data, Sensor


client = mqtt.Client(client_id='server', clean_session=False)


def on_connect(client, userdata, flags, rc):
    print(f'Connect to result code {rc}')
    client.subscribe('aqua/data')
    client.subscribe('cse/iot')


def on_message(client, userdata, msg):
    data = str(msg.payload.decode('utf-8'))
    data = json.loads(data)

    if msg.topic == 'aqua/data':
        sensor = Sensor.objects.get(name=data['sensor'])
        Data.objects.create(sensor=sensor, temp=data['temp'], ph=data['ph'], tds=data['tds'])

    if msg.topic == 'cse/iot':
        sensor = Sensor.objects.get(name=data['sensor'])
        ClassData.objects.create(sensor=sensor, temp=data['temp'], tur=data['tur'], dis=data['dis'], count=data['count'])

def mqtt_start():
    global client
    try:
        client.loop_forever(retry_first_connection=True)
    except json.JSONDecodeError:
        client.loop_forever(retry_first_connection=True)


def mqtt_setup():
    global client
    client.on_connect = on_connect
    client.on_message = on_message

    broker = settings.MQTT_HOST_NAME
    port = settings.MQTT_PORT
    client.connect(broker, port, 60)
    client.reconnect_delay_set(min_delay=1, max_delay=2000)


def mqtt_run():
    mqtt_setup()
    mqtt_thread = Thread(target=mqtt_start)
    mqtt_thread.start()


def mqtt_test():
    mqtt_setup()
    mqtt_start()


if __name__ == '__main__':
    mqtt_test()
