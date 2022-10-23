from lib2to3.pytree import convert
import paho.mqtt.client as mqtt
import time
from random import randrange, uniform
import base64
import pickle

from cryptography.fernet import Fernet

# f_keys = open("keys.pkl", "rb")
# keys = pickle.load(f_keys)

key = b'sDPwjSlr6uHHuH8ezqzjZBJau8dTShpPHWxwkDvVf-c='
fernet = Fernet(key)
fernet2 = Fernet(key)



# token = f.encrypt(b"my deep dark secret")

mqttBroker = "test.mosquitto.org"
client = mqtt.Client("Car_Data")
client.connect(mqttBroker)

while(True):
    f = open("1.jpg", "rb")
    filecontent = f.read()
    byteArr = fernet.encrypt(filecontent)

    msg = {
        "id": "car_00",
        "body": byteArr
    }

    # print(key, fernet2.decrypt(msg["body"]))
    # pkl = pickle.dumps(msg)

    client.publish("IMAGE_DATA", str(msg), retain=True)
    print("Uploading: Image Data")
    time.sleep(10) 