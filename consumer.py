import paho.mqtt.client as paho

def on_message(mosq, obj, msg):
    print("%-20s %d -> %s" % (msg.topic, msg.qos, msg.payload.decode("utf-8")))

if __name__ == 'main':
    client = paho.Client()
    client.on_message = on_message
    client.connect("192.168.1.9", 1883, 60)
    client.subscribe("/pos/sensor/umidade/cozinha", 0)

    while client.loop() == 0:
        pass