# https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

import signal
import sys
from paho.mqtt import client as mqtt_client


broker = 'test.mosquitto.org'
port = 1883
topic = "VarunChugh1"
client_id = "VarunChugh"

fileName = "IMUData.csv"

file = open(fileName, "w")
print("Created file")


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # Set Connecting Client ID
    client = mqtt_client.Client(client_id, clean_session=True)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        message = msg.payload.decode()
        if len(message) < 100:
            print(message)
            file.write(message + "\n")


    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


def starter():
    i = 0

    file.write("AccX,AccY,AccZ,GyroX,GyroY,GyroZ,Roll,Pitch\n")

    while i < 500:  # Adds arbitrary data that to be Processed by the Butterworth Filter
        file.write(f"0,0,1,0,0,0,0,0\n")
        i += 1



def mqtt_transmission():
    client = connect_mqtt()
    try:
        starter()
        run()
    except:
        client.disconnect()
        client.loop_stop()
        file.close()
        print('finished')


