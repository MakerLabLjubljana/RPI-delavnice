import RPi.GPIO as GPIO
import requests
import time

BtnPin = 18
LedPin = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(LedPin, GPIO.OUT)

OLDinput_state = 0

while True:
    input_state = GPIO.input(BtnPin)
    if input_state == False and input_state!=OLDinput_state:
        print('Button Pressed')
        GPIO.output(LedPin,True)
        time.sleep(0.2)
	r = requests.post("https://maker.ifttt.com/trigger/button_pressed/with/key/csB_0GMzOkFL2Fn7xvS7D3", data = {"value1":"3"})

	print r
	
    if input_state == True and input_state!=OLDinput_state:
        GPIO.output(LedPin,False)


    OLDinput_state = input_state


