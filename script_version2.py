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

print ("connection established...")

while 1:
	
		text = input()
		sock.send(bytes(text, 'UTF-8'))

		if text == "2": # receive data
			data = ""
			while 1: 
				try:
					data += sock.recv(1024).decode('utf-8')
					data_end = data.find('\n')
					if data_end != -1:
						rec = data[:data_end]
						print (data)
						data = data[data_end+1:]
						break 
				except KeyboardInterrupt:
					break
		if text == "exit":
			break
sock.close()
print ("end connection...")






