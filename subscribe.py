import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Forbundet til broker!")
        client.subscribe("pilledata")
    else:
        print(f"Forbindelsesfejl med kode {rc}")

def on_message(client, userdata, msg):
    print(f"Besked modtaget: {msg.payload.decode()} på emne: {msg.topic}")


broker_ip = "172.20.10.7" 
client = mqtt.Client()


client.on_connect = on_connect
client.on_message = on_message

try:
    print(f"Forbinder til MQTT broker på {broker_ip}...")
    client.connect(broker_ip, 1883, 60)
    client.loop_forever()
except Exception as e:
    print(f"Der opstod en fejl: {e}")
