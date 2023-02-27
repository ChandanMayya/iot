import socket 
#client


import RPi.GPIO as GPIO
#import Adafruit_MCP3008
#import Adafruit_GPIO.SPI as SPI
import time

Buzzer=36

HOST='192.168.14.41'
PORT=5500
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Buzzer,GPIO.OUT)
GPIO.setwarnings(False)
try:
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
		s.connect((HOST,PORT))
		while True:
			data=s.recv(1024).decode('utf-8')
			print(data)
			if(str(data)=="Alert"):
				print("Alert: Gas Leakage detected...")
				GPIO.output(Buzzer,True)
				time.sleep(3)
				GPIO.output(Buzzer,False)
				time.sleep(3)
except KeyboardInterrupt:
	s.close()
	GPIO.cleanup()
