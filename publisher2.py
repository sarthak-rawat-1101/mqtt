import paho.mqtt.client as mqtt
import time
from random import randrange, uniform

mqttBroker = "test.mosquitto.org"
client = mqtt.Client("Company_Data")
client.connect(mqttBroker)

while(True):
    randNumber = uniform(1, 2)
    obj = {
        "name": "Firmware Update",
        "id": randNumber
    }
    client.publish("FIRMWARE_UPDATE", str(obj), retain=True)
    print("Uploading: " + str(obj) + " to Firmware")
    time.sleep(1)