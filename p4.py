#program 4
import RPi.GPIO as gpio
import time

relay=38

gpio.setmode(gpio.BOARD)
gpio.setup(relay,gpio.OUT,initial=0)

try:
	    #while(True):
		print("Begin of Program")
		gpio.output(relay, True)
		print("relay on")
		time.sleep(2)
		gpio.output(relay, False)
		time.sleep(2)
		print("relay off")
except KeyboardInterrupt:
	gpio.cleanup()
	print("End of prog")
