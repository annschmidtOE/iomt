import paho.mqtt.client as mqtt


broker_address = "172.20.10.7"  
port = 1883  
topic = "test/emne"  


message = "Hej fra Raspberry Pi!"

def main():
    try:
        
        client = mqtt.Client()

        
        print(f"Forbinder til MQTT broker på {broker_address}:{port}...")
        client.connect(broker_address, port=port)

        
        print(f"Sender besked til emne '{topic}': {message}")
        client.publish(topic, message)

    
        client.disconnect()
        print("Besked sendt og forbindelse lukket.")
    except Exception as e:
        print(f"Der opstod en fejl: {e}")

if __name__ == "__main__":
    main()
