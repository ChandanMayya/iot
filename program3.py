#program 3
import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

led1 = 15
led2=13

gpio.setup(led1,gpio.OUT,initial=1)
gpio.setup(led2,gpio.OUT,initial=1)


files=open("file1.txt")
on=int(files.readlines(1)[0].split("=")[1])
off=int(files.readlines(2)[0].split("=")[1])

try:
	while(True):
		gpio.output(led1,False)
		gpio.output(led2,True)
		time.sleep(on)
		gpio.output(led1,True)
		gpio.output(led2,False)
		time.sleep(off)
except KeyboardInterrupt:
	gpio.cleanup()
