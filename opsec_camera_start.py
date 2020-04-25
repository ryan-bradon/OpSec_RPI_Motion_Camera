from subprocess import call
import time
import RPi.GPIO as GPIO

# Just Updated 04/23/2020


# Initialize GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(04, GPIO.IN)   # GPIO4 is pin 7
CAMERA_INTERVAL = 1
SENSOR_INTERVAL = 0.25

# wait for proximity sensor 
while True:
	if (GPIO.input(04)):
		try:
			# Take a picture
			call("raspistill -e jpg --vflip -q 100 -o snapshot_{int(time.time())}.jpg", shell=True)
		except Exception as e:
			print(f"Unexpected error:\n{str(e)}")
		time.sleep(CAMERA_INTERVAL)
	else:
		time.sleep(SENSOR_INTERVAL)


