import requests
from thingspeak import Channel
from mqtt_bridge import MqttHttpThingSpeakBridge

proxies = {
           'http': 'http://user:password@host:port',
           'https': 'http:////user:password@host:port',
            }

server = "172.16.245.63"
username = ''
password = ''
client_id = ''
thing_speak_api_key = 

s = requests.Session()
s.proxies = proxies
ch = Channel(api_key=thing_speak_api_key, connection=s)
bridge = MqttHttpThingSpeakBridge(client_id, server, username, password, ch)
bridge.connect()
