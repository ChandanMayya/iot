import RPi.GPIO as gpio
import time
import datetime

led=13

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(led,gpio.OUT,initial=0)
gpio.setup(led,gpio.OUT)
from flask import Falsk,render_template
app=Falsk(__name__)

light_status=="OFF"
def glow_led(event):
	print("....")
	global light_status
	if event==switch1 and light_status=="OFF":
		gpio.OUTPUT(led,False)
		light_status=="ON"
	elif event==switch1 and light_status=="ON":
		gpio.OUTPUT(led,True)
		light_status=="OFF"  
@app.route('/')
def hello_world():
	return render_template('web.html')
@app.route('/redledon')
def redledon():
	GPIO.output(13,gpio.LOW)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M")
	templateData={'lstatus':'ON','time':timeString}
	return render_template('web.html',**templateData)
@app.route('/redledoff')
def redledoff():
	GPIO.output(13,gpio.HIGH)
	GPIO.output(relay,False)
	GPIO.output(buzzer,False)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M")
	templateData={'lstatus':'OFF','time':timeString}
	return render_template('web.html',**templateData)
	
