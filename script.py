####################################
# File name: script.py             #
# Version: 1                       #
# Author: Rui Oliveira             #
# Email: ruipedrooliveira@ua.pt    #
# Date create: 29-03-2017          #
# Date last modified: 29-03-2017   #
# Python Version: 2.7              #
####################################

#!/usr/bin/python

import requests
import json
from time import sleep
import serial

def post_value(value, id_sensor):
	authentication = ('roliveira', 'ro1993194')
	login_payload = {'value': value}
	url = 'http://127.0.0.1:8000/api/reading/'+str(id_sensor)
	response = requests.post(url, data=login_payload,auth=authentication)


# type_info: seding_time status_sm baterry_sm
def get_info_sm(id_sm_or_name, type_info): # in minutos
	url = 'http://127.0.0.1:8000/api/cm/'	
	response = requests.get(url, headers={'Authorization': 'Token 7467cb944f696b9d848a78c68025468cb962f68a'} )
	data = response.json()
	print data#[str(type_info)]


#post_value(1213,47)
#
#get_info_sm('arduino_nano','seding_time')


#read usb port 


def read_arduino(pathUSB)
	# Establish the connection on a specific port
	ser = serial.Serial(pathUSB, 9600) 

	print ser.readline() # Read the newest output 


read_arduino('/dev/ttyUSB0')
get_info_sm('dsa','name')