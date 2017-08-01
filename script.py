####################################
# File name: script.py             #
# Version: 1                       #
# Author: Rui Oliveira             #
# Email: ruipedrooliveira@ua.pt    #
# Date create: 29-03-2017          #
# Date last modified: 01-08-2017   #
# Python Version: 3                #
####################################

#!/usr/bin/python

import time, sys
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
id_sensor_valve = 18

target_name = "HC-06"
target_address = None 
port = 1
response_last_time = None
response_last_status = None

def get_seding_time(id_sm): # in minutos
	url = 'http://192.168.160.20/api/sm/'+str(id_sm)
	global response_last_time

	try:
		response = requests.get(url, headers=auth ) 
		response_last_time = response
	except requests.ConnectionError:
		response = response_last_time

	data = response.json()
	return data['seding_time']


def read_value_in_sensor(value, id_sensor):
	login_payload = {'value': value}
	url = 'http://192.168.160.20/api/reading/'+str(id_sensor)
	response = requests.post(url, 
		data=login_payload,
		headers=auth)
	
def get_status_valve(id_sensor_valve): # in minutos
	url = 'http://192.168.160.20/api/sensor/'+str(id_sensor_valve)
	
	global response_last_status

	try:
		response = requests.get(url, headers=auth ) 
		response_last_status = response
	except requests.ConnectionError:
		response = response_last_status
		
	data = response.json()
	
	state = 0 
	if str(data[0]['status_actuator']) == "True": 
		state = 1

	return state


def controllerValve(socket_bluetooth):
	last_status =0
	while 1 :
		status = get_status_valve(id_sensor_valve)
		#status = random.getrandbits(1) # with debug
		
		#send status if status is not equal last status 		
		if status != last_status: 
			socket_bluetooth.send(bytes(str(status), 'UTF-8'))
			last_status=status
			print ("Send.. "+str(status)) 
		
		#time.sleep(1) #debug

def receiveData(socket_bluetooth,request_data_op):
	while 1 :
		socket_bluetooth.send(bytes(request_data_op, 'UTF-8'))
		print ("request data")

		data = ""	
		while 1:
			try:
				data += socket_bluetooth.recv(1024).decode('utf-8')
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
	    sys.exit(0)

	for services in bluetooth.find_service(address = target_address):
		print (" Port: %s" % (services["port"]))

	socket_bluetooth = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
	socket_bluetooth.connect((target_address,port))
	
	print ("connection established...")
	request_data_op = "2"

	thread_controller = Thread(target=controllerValve, args=[socket_bluetooth])

	thread_receiveData = Thread(target=receiveData, args=[socket_bluetooth,request_data_op])

	print ("Start thread controller")
	thread_controller.start()

	print ("Start thread receive data")
	thread_receiveData.start()