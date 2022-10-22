import paho.mqtt.client as mqtt
import time
import base64

import numpy as np

import sys # to access the system
import cv2
import pickle
from cryptography.fernet import Fernet

f_keys = open("keys.pkl", "rb")
keys = pickle.load(f_keys)


def on_message(client, userdata, message):
    recvd_obj = eval(str(message.payload.decode("utf-8"))) #pickle.loads(message.payload)

    key = keys[recvd_obj["id"]]
    emsg = recvd_obj["body"]
    fernet = Fernet(key)
    msg = fernet.decrypt(emsg) # decrypted image
    
    nparr = np.fromstring(msg, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print("Image Received")
    
    while True:
        cv2.imshow("Sheep", img_np)
        cv2.waitKey(0)
        sys.exit() # to exit from all the processes

    cv2.destroyAllWindows() # destroy all windows

mqttBroker = "test.mosquitto.org"
client = mqtt.Client("Car", clean_session=False)
client.connect(mqttBroker)

client.subscribe("IMAGE_DATA")
client.on_message = on_message

client.loop_forever()