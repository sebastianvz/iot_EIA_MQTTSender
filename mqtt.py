import paho.mqtt.client as mqtt #import the client1
import time
import random
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################
broker_address="iottest45.cloud.shiftr.io"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("device9") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.username_pw_set("iottest45", "nFkl77W5JqpvzAXg")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
while True:
    value_volt = random.uniform(123.1,126.9)
    client.publish("Termofijadora01/fase1/voltaje",str(round(value_volt, 2)))
    print("se envia")
    value_curr= random.uniform(33.1,36.5)
    client.publish("Termofijadora01/fase1/corriente",str(round(value_curr, 2)))
    time.sleep(5)