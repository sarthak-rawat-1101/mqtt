from cryptography.fernet import Fernet
import mqtt
import pickle
import json

mqtt.connect("cloud_server")

# publish updates
def push_updates(topic, file_name):
    file_content = open(file_name, "rb").read()
    mqtt.publish(topic, str(file_content))

# sub to a topic "cars"
"""
{
    "sender_id",
    "message_type",
    "message"
}
"""
def listen(topic):
    def on_message(client, userdata, message):
        # recvd_obj = eval(str(message.payload.decode("utf-8")))
        # recvd_obj = message.payload.decode("utf-8")
        # recvd_obj = message.payload
        try:
            # print(recvd_obj)
            print(message.payload[50:100])
            recvd_obj = pickle.loads(bytes(message.payload))
        except Exception as e:
            print(e)
            return
        sender_id = recvd_obj["sender_id"]
        message_type = recvd_obj["message_type"]
        message = recvd_obj["message"]

        if message_type == "REQ_MODELS":
            # fetch the model
            # send them back
            pass
        elif message_type == "IMAGE_STREAM":
            # display images
            print(sender_id, message_type)
            # display as video
            pass
        elif message_type == "FETCH_PROFILES":
            pass
        else:
            pass
         
    mqtt.subscribe(topic, on_message)

    # respond with a command
    # store data in db
    # send ai models

if __name__ == "__main__":
    # push_updates("updates", "cloud_server/update_files.zip")
    listen("CLOUD_SERVER")
