import paho.mqtt.client as mqtt

mqttBroker = "test.mosquitto.org"

def connect(client_id):
    client = mqtt.Client(client_id)
    client.connect(mqttBroker)

def publish(topic, data):
    client.publish(topic, str(data), retain=True)

def subscribe(topic, on_message):
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()
