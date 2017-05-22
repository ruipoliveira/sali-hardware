2####################################
# File name: script.py             #
# Version: 1                       #
# Author: Rui Oliveira             #
# Email: ruipedrooliveira@ua.pt    #
# Date create: 29-03-2017          #
# Date last modified: 26-04-2017   #
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
import commands

auth={'Authorization': 'Token a9f6b9abaa2519650a7625d78c3f52eb1c629f08'}

id_sensor_temperature = 8
id_sensor_level = 10
id_sensor_luminosity = 9
id_sensor_valve = 11
id_sm = 5 


def read_value_in_sensor(value, id_sensor):
	login_payload = {'value': value}
	url = 'http://192.168.160.20/api/reading/'+str(id_sensor)
	response = requests.post(url, 
		data=login_payload,
		headers=auth)


def get_baterry_percentage(): 
    
    c = 'upower -i /org/freedesktop/UPower/devices/battery_BAT0'
    output = commands.getstatusoutput(c)
    
    after_perc = output[1].split('percentage: ')[1].strip()

    index = after_perc.find('%')

    return after_perc[:index]


def get_seding_time(id_sm): # in minutos
	url = 'http://192.168.160.20/api/sm/'+str(id_sm)
	response = requests.get(url, headers=auth )
	data = response.json()
	return data['seding_time']
	


def read_data_arduino(pathUSB):
	ser = serial.Serial(
	    port=pathUSB,
	    baudrate=9600,
	    parity=serial.PARITY_ODD,
	    stopbits=serial.STOPBITS_TWO,
	    bytesize=serial.SEVENBITS
	)


	ser.readline() 
	while True:
		#ser.write(str(random.randint(0, 1)))
		print ser.readline() 
		#print ser.readline()

		
		# <TEMPERATURE>;<LEVEL WATER>;<LUMINOSITY>;<WATER VALVE> 

		t = time.strftime("%Y-%m-%d %H:%M")


		data_split = ser.readline().split(';')


		print time.strftime("%Y-%m-%d %H:%M")
		print 'TEMPERATURE = '+str(data_split[0])
		read_value_in_sensor(data_split[0], id_sensor_temperature)

		print 'LEVEL WATER = '+str(data_split[1])
		read_value_in_sensor(data_split[1], id_sensor_level)

		print 'LUMINOSITY = '+str(data_split[2])
		read_value_in_sensor(data_split[2], id_sensor_luminosity)

		print 'WATER VALVE = '+str(data_split[3])
		read_value_in_sensor(data_split[3], id_sensor_valve)

		print 'BATERIA: '+str(get_baterry_percentage()) +'%'

		print '============================='

		time.sleep(60*get_seding_time(id_sm))






#post_value(1213,1)
#
#get_info_sm('arduino_nano','seding_time')


#read usb port 


	

######## to run... ########
read_data_arduino('/dev/ttyUSB0')
#print get_baterry_percentage()



######## testing... ########


#get_info_sm(); 

#get_seding_time(2)


#while True:
#	print time.strftime("%Y-%m-%d %H:%M")
#	read_value_in_sensor(random.randint(0, 100), id_sensor_temperature)
#	read_value_in_sensor(random.randint(0, 100), id_sensor_luminosity)
#	print "outro...."
#	time.sleep(60*get_seding_time(2))
