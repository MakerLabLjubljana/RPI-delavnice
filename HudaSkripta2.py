import RPi.GPIO as GPIO
import time

LedPin = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(LedPin, GPIO.OUT)

while True:
    GPIO.output(LedPin, True)
    print("ON")
    time.sleep(1)
    GPIO.output(LedPin, False)
    print("OFF")
    time.sleep(1)
    
