
import time
from threading import Thread

def controllerValve():
    while 1 :
	    print "eiii controle "
	    time.sleep(20)

def receiveData():
	while 1 :
		print "sendddd cenas"
		time.sleep(5)


if __name__ == "__main__":

	thread_controller = Thread(target=controllerValve)

	thread_receiveData = Thread(target=receiveData)

	print "Start thread controller"
	thread_controller.start()

	print "Start thread receive data"
	thread_receiveData.start()