import paho.mqtt.client as mqtt 
import time
import random
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################
broker_address="host"
print("creating new instance")
client = mqtt.Client("device9") 
client.on_message=on_message 
print("connecting to broker")
client.username_pw_set("username", "password")
client.connect(broker_address)
client.loop_start() 
while True:
    value_volt = random.uniform(123.1,126.9)
    client.publish("topic/innertopic",str(round(value_volt, 2)))
    print("se envia")
    time.sleep(2)
