import bluetooth
import socket

target_name = "HC-06"
target_address = None 
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


for services in bluetooth.find_service(address = target_address):
	print (" Port: %s" % (services["port"]))


sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
sock.connect((target_address,port))

sock.bind(("",port))
sock.listen(1)
client_sock,address = sock.accept()

print ("connection established...")

while 1:
    text = input()

    if text == "2": # receive data
    	data = client_sock.recv(1024)
		print ("received [%s]" % data)

    if text == "quit":
        break
    sock.send(bytes(text, 'UTF-8'))
 
sock.close()



