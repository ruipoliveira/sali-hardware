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
import time 
import serial
from serial import Serial, SEVENBITS, STOPBITS_ONE, PARITY_EVEN
from unidecode import unidecode
import string
import random


auth={'Authorization': 'Token a9f6b9abaa2519650a7625d78c3f52eb1c629f08'}





def read_value_in_sensor(value, id_sensor):
	login_payload = {'value': value}
	url = 'http://127.0.0.1:8000/api/reading/'+str(id_sensor)
	response = requests.post(url, 
		data=login_payload,
		headers=auth)




# type_info: seding_time status_sm baterry_sm
def get_info_sm(id_sm_or_name, type_info): # in minutos
	url = 'http://192.168.160.20/api/cm/'
	response = requests.get(url, headers=auth )
	data = response.json()
	print data#[str(type_info)]


def read_valve(id_valve):


#post_value(1213,1)
#
#get_info_sm('arduino_nano','seding_time')


#read usb port 



def read_arduino(pathUSB):

	ser = serial.Serial(
	    port=pathUSB,
	    baudrate=9600,
	    parity=serial.PARITY_ODD,
	    stopbits=serial.STOPBITS_TWO,
	    bytesize=serial.SEVENBITS
	)


	id_sensor_temperatura = 
	id_sensor_level = 
	id_sensor_luminosidade = 
	id_sensor_valve = 

	ser.readline() 
	while True:
		#ser.write(str(random.randint(0, 1)))
		
		#out = ''
		

		##ser.write(str(random.randint(0, 1)))

		#print ser.readline()
		data_split = ser.readline().split(';')

		print time.strftime("%Y-%m-%d %H:%M")
		print 'temperatura = '+str(data_split[0])
		read_value_in_sensor(data_split[0], id_sensor_temperatura)

		print 'Level = '+str(data_split[1])
		read_value_in_sensor(data_split[1], id_sensor_level)

		print 'Luminosidade = '+str(data_split[2])
		read_value_in_sensor(data_split[2], id_sensor_luminosidade)

		print 'Valve = '+str(data_split[3])
		read_value_in_sensor(data_split[3], id_sensor_valve)

		print '============================='



		#time.sleep(1)







#ser.write(str(random.randint(0, 1)))

#time.sleep(1)

#msg = ser.read(ser.inWaiting())
#print msg 

#sleep(10)

#while True:

#

#print ser.readline()
#date_split = data.split(';')

"""
print time.strftime("%Y-%m-%d %H:%M")
print 'Luminosidade = '+str(date_split[0])
print 'temperatura = '+str(date_split[1])
print 'Level = '+str(date_split[2])
print 'Valve = '+str(date_split[3])
print '============================='
"""

#sleep(1)


# <luminosidade>;<temperatura>;<nivel>;<valvula> 

read_arduino('/dev/ttyUSB3')
#get_info_sm('dsa','name')




#while True: 
	#data = ser.readline()
	#print data
