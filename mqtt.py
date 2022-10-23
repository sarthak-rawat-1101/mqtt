import paho.mqtt.client as mqtt

mqttBroker = "test.mosquitto.org"
client = None
def connect(client_id):
    global client
    client = mqtt.Client(client_id)
    client.connect(mqttBroker)

def publish(topic, data):
    global client
    client.publish(topic, data, retain=True)

def subscribe(topic, on_message):
    global client
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()
