import RPi.GPIO as gpio
import time
import datetime

led1=15
led2=13
switch1 = 35 
switch2 = 37 
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(led1,gpio.OUT,initial=1)
gpio.setup(led2,gpio.OUT,initial=1)
gpio.setup(switch1,gpio.IN)
gpio.setup(switch2,gpio.IN)
light_status="OFF"

def glow_led(event):
	global light_status
	if event==switch1:
		gpio.output(led1,False)
		light_status="ON"
	elif event==switch2:
		gpio.output(led1,True)
		light_status="OFF"
		
gpio.add_event_detect(switch1,gpio.RISING,callback=glow_led,bouncetime=1)

gpio.add_event_detect(switch2,gpio.RISING,callback=glow_led,bouncetime=1)


from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def ledstatus():
	now=now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M")
	templateData={'lstatus':light_status,'time':timeString}
	return render_template('lightstatus.html',**templateData)
if __name__ == "__main__":
	app.run(debug=True,port=4000,host='192.168.14.42')

