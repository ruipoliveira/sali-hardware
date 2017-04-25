import serial
import random

ser = serial.Serial(
    port='/dev/ttyUSB3',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

ser.write(str(random.randint(0, 1)))