
import json
import time
import paho.mqtt.client as paho
from paho import mqtt


# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    from .models import Payload
    byte_str = msg.payload
    print(byte_str, type(byte_str))
    dict_str = byte_str.decode('utf-8')
    my_data = json.loads(dict_str)
    Payload.objects.create(device_serial=my_data['device_serial'], temperature=my_data['temperature'], humidity=my_data['humidity'], error=my_data['error'], lat=my_data['lat'], lon=my_data['lon'])

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
# client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("koki014", "2525244Koki")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("eac64e5a30d44bca97d7cc32e4e1446e.s1.eu.hivemq.cloud", 8883)
# client.connect_async('localhost', port=1883, keepalive=60, bind_address="")


# setting callbacks, use separate functions like above for better visibility
# client.on_subscribe = on_subscribe
client.on_message = on_message
# client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("#", qos=1)

# a single publish, this can also be done in loops, etc.
# client.publish("encyclopedia/temperature", payload="hot", qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
# client.loop_start()
