import paho.mqtt.client as mqtt

mqttBroker = "test.mosquitto.org"

def connect(client_id):
    client = mqtt.Client(client_id)
    client.connect(mqttBroker)

# overwrite this
# def on_message(client, userdata, message):
#     recvd_obj = eval(str(message.payload.decode("utf-8")))

def subscribe(topic, on_message):
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()


