import paho.mqtt.client as mqtt

# MQTT-konfiguration
broker_address = "172.20.10.7"  # Erstat med din VM's IP-adresse
port = 1883  # Standardport for MQTT
topic = "test/emne"  # Dit valgte emne

# Besked, der skal sendes
message = "Hej fra Raspberry Pi!"

def main():
    try:
        # Opret en MQTT-klient
        client = mqtt.Client()

        # Forbind til brokeren
        print(f"Forbinder til MQTT broker på {broker_address}:{port}...")
        client.connect(broker_address, port=port)

        # Publicer beskeden
        print(f"Sender besked til emne '{topic}': {message}")
        client.publish(topic, message)

        # Afbryd forbindelsen
        client.disconnect()
        print("Besked sendt og forbindelse lukket.")
    except Exception as e:
        print(f"Der opstod en fejl: {e}")

if __name__ == "__main__":
    main()
