from cryptography.fernet import Fernet
import mqtt

# TO:DO use env variables
key = b'sDPwjSlr6uHHuH8ezqzjZBJau8dTShpPHWxwkDvVf-c='
fernet = Fernet(key)

mqtt.connect()

def send_image(topic, file_name):
    f = open(file_name, "rb")
    filecontent = f.read()
    byteArr = fernet.encrypt(filecontent)
    msg = {
        "id": "car_00",
        "body": byteArr
    }
    mqtt.publish(topic, str(msg))

def send_dict(topic, msg):
    mqtt.publish(topic, str(msg))

def fetch_updates(topic):
    def on_message(client, userdata, message):
        # zip file
        recvd_obj = eval(str(message.payload.decode("utf-8")))
        # save this file
        # start update routine

    mqtt.subscribe(topic, on_message)

if __name__ == "__main__":
    pass
    '''
    

    
    '''
