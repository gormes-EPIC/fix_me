import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(21, GPIO.IN) 
GPIO.setwarnings(False)
p = GPIO.PWM(16, 100)

i = GPIO.input(21)
while True:
	if GPIO.input(21) == GPIO.LOW:
		p.start(50)
	elif GPIO.input(21) == GPIO.HIGH:
		p.stop()
	
GPIO.cleanup()
