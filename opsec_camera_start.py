from subprocess import call
import time
import RPi.GPIO as GPIO


# Initialize GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(04, GPIO.IN)   # GPIO4 is pin 7
SLEEP_DURATION = 1

# wait for proximity sensor 
while True:
	if (GPIO.input(04)):
		try:
			# Take a picture
			call("raspistill -e jpg --vflip -q 100 -o /tmp/snapshot.jpg", shell=True)
		except Exception as e:
			print(f"Unexpected error:\n{str(e)}")
		time.sleep(SLEEP_DURATION)
	else:
		time.sleep(0.25)


