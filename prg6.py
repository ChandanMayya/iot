import RPi.GPIO as GPIO
import time
import datetime
from time import sleep
led=13
relay=38
buzzer=36
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT,initial=0)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzzer,False)
GPIO.setup(relay,False)

from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def hello_world():
	return render_template('web.html')
@app.route('/redledon')
def redledon():
	GPIO.output(13,GPIO.LOW)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M")
	templateData={'lstatus':'ON','time':timeString}
	return render_template('web.html',**templateData)
@app.route('/redledoff')
def redledoff():
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(relay,False)
	GPIO.output(buzzer,False)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M")
	templateData={'lstatus':'OFF','time':timeString}
	return render_template('web.html',**templateData)
	
@app.route('/buzzeron')
def buzzeron():
	GPIO.output(buzzer,True)
	GPIO.output(buzzer,True)
	sleep(0.2)
	GPIO.output(buzzer,False)
	sleep(0.2)
	GPIO.output(buzzer,True)
	sleep(0.18)
	GPIO.output(buzzer,False)
	sleep(0.18)
	GPIO.output(buzzer,True)
	sleep(0.14)
	GPIO.output(buzzer,False)
	sleep(0.14)
	GPIO.output(buzzer,True)
	sleep(0.10)
	GPIO.output(buzzer,False)
	sleep(0.10)
	GPIO.output(buzzer,True)
	sleep(0.06)
	GPIO.output(buzzer,False)
	sleep(0.6)
	GPIO.output(buzzer,True)
	sleep(0.2)
	GPIO.output(buzzer,False)
	sleep(0.2)
	GPIO.output(buzzer,True)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M")
	templateData1={'bstatus':'ON','time':timeString}
	return render_template('web.html',**templateData1)
@app.route('/buzzerof')
def buzzerof():
	GPIO.output(buzzer,False)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M")
	templateData1={'bstatus':'OFF','time':timeString}
	return render_template('web.html',**templateData1)
@app.route('/relayon')
def relayon():
	GPIO.output(relay,True)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M")
	templateData2={'rstatus':'ON','time':timeString}
	return render_template('web.html',**templateData2)

@app.route('/relayof')
def relayof():
	GPIO.output(relay,False)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M")
	templateData2={'rstatus':'OFF','time':timeString}
	return render_template('web.html',**templateData2)
if __name__ == "__main__":
	app.run(debug=True,port=4000,host='127.0.0.1')
