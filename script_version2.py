
import bluetooth
import socket

target_name = "HC-06"
target_address = None //the address from the Arduino sensor
port = 1

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print ("found target bluetooth device with address "+ target_address)
else:
    print ("could not find target bluetooth device nearby")


sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
sock.connect((target_address,port))


print ("ligado...")

#while 1:
#        tosend = raw_input()
#        if tosend != 'q':
#                sock.send(tosend)
#        else:
#                break
 
sock.close()



