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


"""
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

ser.write(str(sys.argv[1]))



"""
auth={'Authorization': 'Token a9f6b9abaa2519650a7625d78c3f52eb1c629f08'}

id_sensor_valve = 18

id_sm = 5 



def get_status_valve(id_sensor_valve): # in minutos
	url = 'http://192.168.160.20/api/sensor/'+str(id_sensor_valve)
	response = requests.get(url, headers=auth )
	data = response.json()
	
	state = 0 
	if str(data[0]['status_actuator']) == "True": 
		state = 1

	return state



print get_status_valve(id_sensor_valve)