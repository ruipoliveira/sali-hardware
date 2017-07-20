
import time
from threading import Thread
import bluetooth
import socket
import requests
import json
from time import sleep
import string
import random

auth={'Authorization': 'Token a9f6b9abaa2519650a7625d78c3f52eb1c629f08'}

id_sensor_temperature = 15
id_sensor_level = 17
id_sensor_luminosity = 16
id_sensor_valve = 18
id_sm = 8

target_name = "HC-06"
target_address = None 
port = 1

def get_seding_time(id_sm): # in minutos
	url = 'http://192.168.160.20/api/sm/'+str(id_sm)
	response = requests.get(url, headers=auth )
	data = response.json()
	return data['seding_time']


def read_value_in_sensor(value, id_sensor):
	login_payload = {'value': value}
	url = 'http://192.168.160.20/api/reading/'+str(id_sensor)
	response = requests.post(url, 
		data=login_payload,
		headers=auth)
	

def controllerValve(sock):
    while 1 :
	    print ("eiii controle ")
	    time.sleep(20)

def receiveData(sock):
	while 1 :
sock.send(bytes(request_data, 'UTF-8'))
		print ("request data")

		data = ""
		while 1:
			try:
				data += sock.recv(1024).decode('utf-8')
				data_end = data.find('\n')
				if data_end != -1:
					rec = data[:data_end]
					data_split = data.rstrip().split(';')
					print (time.strftime("%Y-%m-%d %H:%M"))
					print ("TEMPERATURE = "+str(data_split[0]))
					read_value_in_sensor(data_split[0], id_sensor_temperature)
					print ('LEVEL WATER = '+str(data_split[1]))
					read_value_in_sensor(data_split[1], id_sensor_level)
					print ('LUMINOSITY = '+str(data_split[2]))
					read_value_in_sensor(data_split[2], id_sensor_luminosity)
					print ('WATER VALVE = '+str(data_split[3]))
					read_value_in_sensor(data_split[3], id_sensor_valve)
					print ('=============================')
					data = data[data_end+1:]
					break 
			except KeyboardInterrupt:
				break

		time.sleep(60*get_seding_time(id_sm))


if __name__ == "__main__":

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
	status = "1" 
	request_data = "2"


	thread_controller = Thread(target=controllerValve, args=[sock])

	thread_receiveData = Thread(target=receiveData, args=[sock])

	print ("Start thread controller")
	thread_controller.start()

	print ("Start thread receive data")
	thread_receiveData.start()