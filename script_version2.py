
import bluetooth
import socket

target_name = "HC-06"
target_address = None 
port = 0

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print ("found target bluetooth device with address "+ target_address)
else:
    print ("could not find target bluetooth device nearby")


for services in bluetooth.find_service(address = target_address):
	print (" Port: %s" % (services["port"]))


sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
sock.connect((target_address,port))

print ("connection established...")

while 1:
	tosend = raw_input()
	if tosend != 'q':
		sock.send(tosend)
	else:
		break
 
sock.close()



