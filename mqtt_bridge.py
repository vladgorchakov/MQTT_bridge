from paho.mqtt import client as mqtt
import json


class MqttHttpThingSpeakBridge:
    def __init__(self, client_id, server, username, password, channel):
        self.server = server
        self.client = mqtt.Client(client_id=client_id)
        self.client.username_pw_set(username, password)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.channel = channel
    

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        # client.subscribe("$SYS/#")
        

    def show_messages(self, msg):
        print('_____________________________________________')
        print(f'topic: {msg.topic}')
        print(f'message: {msg.payload}')
        
        
    def on_message(self, client, userdata, msg):
        if msg.topic == "house/ds18b20-1":
            self.show_messages(msg)
            self.channel.write_field(float(msg.payload), 1)
        elif msg.topic == "house/dht11-1":
            self.show_messages(msg)
            data = json.loads(msg.payload)
            self.channel.write_fields({2: data['humidity'], 3: data['temp']})
                     
    
     
    def connect(self):
        self.client.connect(host=self.server)
        self.client.subscribe(topic='bsuir/#')
        self.client.loop_forever()
