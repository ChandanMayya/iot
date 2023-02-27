import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)

led1=15

gpio.setup(led1,gpio.OUT,initial=1)

a=2
b=3
	
try:
	while(True):
		gpio.output(led1,True)
		time.sleep(a)
		gpio.output(led1,False)
		time.sleep(b)
except KeyboardInterrupt:
	gpio.cleanup()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
