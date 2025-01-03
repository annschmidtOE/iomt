import paho.mqtt.client as mqtt
import json

MQTT_BROKER = '172.20.10.5'
INPUT_TOPIC = 'pilledata'
OUTPUT_TOPIC = 'pilledata'
AZURE_BROKER = '172.201.226.158'
AZURE_TOPIC = 'pilledata'

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    # Save the data
    with open('data.log', 'a') as f:
        f.write(f"{msg.payload.decode()}\n")
    # Relay the data
    client.publish(OUTPUT_TOPIC, msg.payload)

client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER)
client.subscribe(INPUT_TOPIC)
client.loop_start()


client = mqtt.Client()
client.on_message = on_message
client.connect(AZURE_BROKER)
client.publish(AZURE_TOPIC)
client.loop_start()



while True:
    pass