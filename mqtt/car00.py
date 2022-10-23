from cryptography.fernet import Fernet
import mqtt
import capture_frames
import pickle
import json

# TO:DO use env variables
id = "car_00"
key = b'sDPwjSlr6uHHuH8ezqzjZBJau8dTShpPHWxwkDvVf-c='
fernet = Fernet(key)

mqtt.connect(id)

def send_frames(topic, frames):
    msg = {
        "id": id,
        "message_type": "IMAGE_STREAM",
        "message_body": frames
    }
    pkl = pickle.dumps(msg)
    mqtt.publish(topic, pkl)
    print(pkl[50:100])

def send_image(topic, file_name):
    f = open(file_name, "rb")
    filecontent = f.read()
    byteArr = fernet.encrypt(filecontent)
    msg = {
        "id": id,
        "body": byteArr
    }
    pkl = pickle.dumps(msg)
    mqtt.publish(topic, pkl)

def send_msg(topic, msg):
    mqtt.publish(topic, str(msg))

def fetch_updates(topic):
    def on_message(client, userdata, message):
        # zip file
        recvd_obj = eval(str(message.payload.decode("utf-8")))
        # save this file
        with open(id + "/update_files.zip", "wb") as f:
            f.write(recvd_obj)
        # start update routine
        print("Downloaded update")

    mqtt.subscribe(topic, on_message)

if __name__ == "__main__":
    # fetch_updates("updates")
    send_frames("CLOUD_SERVER", capture_frames.capture_frames(1))
