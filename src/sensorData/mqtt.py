from threading import Thread
import time
import json

import paho.mqtt.client as mqtt

client = mqtt.Client(client_id='server', clean_session=False)


def on_connect(client, userdata, flags, rc):
    print(f'Connect to result code {rc}')
    client.subscribe('aqua/data')


def on_message(client, userdata, msg):
    print(f'{msg.topic}, {msg.payload}')
    data = str(msg.payload.decode('utf-8'))
    print(msg.topic)
    print(data)
    data = json.loads(data)
    print(data)
    print(data['tds'])
    print(data['temp'])
    print(data['ph'])

    if msg.topic == 'aqua/data':
        pass


def mqtt_start():
    global client
    client.loop_forever(retry_first_connection=True)


def mqtt_setup():
    global client
    client.on_connect = on_connect
    client.on_message = on_message

    broker = '0.0.0.0'
    client.connect(broker, 1883, 60)
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
