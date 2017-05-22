
import bluetooth
import socket

target_name = "HC-06"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print ("found target bluetooth device with address "+ target_address)
else:
    print ("could not find target bluetooth device nearby")


port = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((target_address,port))
print ("ligado...")
#while 1:
#    text = input()
#    if text == "quit":
#        break
#    s.send(bytes(text, 'UTF-8'))
s.close()

