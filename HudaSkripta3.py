import RPi.GPIO as GPIO
import time

BtnPin = 18
LedPin = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(LedPin, GPIO.OUT)


while True:
    input_state = GPIO.input(BtnPin)
    if input_state == False:
        print('Button Pressed')
	GPIO.output(LedPin,True) 
        time.sleep(0.2)
    
    else:
        GPIO.output(LedPin,False)
