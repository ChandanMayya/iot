from picamera import PiCamera
from time import sleep
import datetime
current_date=datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')
camera=PiCamera()
camera.start_preview()
sleep(3)
camera.capture(current_date+'.jpg')
print("Image captured...")
camera.stop_preview()
