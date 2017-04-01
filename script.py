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
	authentication = ('roliveira', 'roliveira1993194')
	login_payload = {'value': value}
	url = 'http://127.0.0.1:8000/api/reading/'+str(id_sensor)
	response = requests.post(url, data=login_payload,auth=authentication)


# type_info: seding_time status_sm baterry_sm
def get_info_sm(id_sm_or_name, type_info): # in minutos
	url = 'http://127.0.0.1:8000/api/sm/'+str(id_sm_or_name)
	response = requests.get(url)
	data = response.json()
	print data[str(type_info)]


#post_value(1213,47)
#
#get_info_sm('arduino_nano','seding_time')


#read usb port 

# Establish the connection on a specific port
ser = serial.Serial('/dev/ttyUSB0', 9600) 

x = 1 while True:
       print ser.readline() # Read the newest output 
       x += 1
