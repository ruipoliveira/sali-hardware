
import time, sys
from threading import Thread
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

response_last = None


def get_seding_time(id_sm): # in minutos
	url = 'http://192.168.160.20/api/sm/'+str(id_sm)
	global response_last

	try:
		response = requests.get(url, headers=auth ) 
		response_last = response
	except requests.ConnectionError:
		response = response_last
		print "valor anterior "

	data = response.json()

	return data['seding_time']



while True: 

	print get_seding_time(id_sm)

	time.sleep(5)



# raspivid -o - -t 0 -vf -hf -fps 30 -b 6000000 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/ux4a-v8x7-3yws-635b

