import RPi.GPIO as GPIO
import time

BEAM_PIN = 17
LED_PIN = 21

def break_beam_callback(channel):
	time.sleep(2)
	if GPIO.input(BEAM_PIN):
		#print("beam unbroken")
		GPIO.output(LED_PIN,GPIO.LOW)
	else:
		print("The blue trash can need to be emptied")
		GPIO.output(LED_PIN,GPIO.HIGH)

GPIO.setmode(GPIO.BCM)

GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.add_event_detect(BEAM_PIN, GPIO.BOTH, callback=break_beam_callback)

message = input("Press enter to quit\n\n")
GPIO.cleanup() 
