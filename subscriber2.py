import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    recvd_obj = str(message.payload.decode("utf-8"))
    #str to dict
    recvd_obj = eval(recvd_obj)
    print(recvd_obj['name'])
    print(recvd_obj['id'])
    # print("Received Image Data: ", str(message.payload.decode("utf-8")))

mqttBroker = "test.mosquitto.org"
client = mqtt.Client("Car2", clean_session=False)
client.connect(mqttBroker)


client.subscribe("FIRMWARE_UPDATE")
client.on_message = on_message

client.loop_forever()


# while True:
#     client.subscribe("FIRMWARE_UPDATE")
#     client.on_message = on_message
#     time.sleep(1)
# client.loop_end()