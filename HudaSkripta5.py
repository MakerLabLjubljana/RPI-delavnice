
import RPi.GPIO as GPIO
import requests
import time

BtnPin = 18
LedPin = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(LedPin, GPIO.OUT)

OLDinput_state = 0

def Parse(r): 
    Done = 0 
    i = len(r)-1
    while(not Done):
	if(r[i]==">" and r[i-1]=="a"):
	    i = i-2
	    j = i-2
	    while(r[j]!='>'):
		if(j<2):
		    return -1
		j-=1
	    Done=1
	i-=1
	if(i<2):
	    return -1
    return r[j+1:i]	



while True:
    input_state = GPIO.input(BtnPin)
    if input_state == False and input_state!=OLDinput_state:
        print('Button Pressed')
        GPIO.output(LedPin,True)
        time.sleep(0.2)
        r = requests.get("http://www.posttestserver.com/data/2015/10/18/cime/?C=M;O=A")

	if(r.status_code == 200):
            LastPostNum = Parse(r.text)
	    if(LastPostNum!=-1):
	    	LastPostData = requests.get("http://www.posttestserver.com/data/2015/10/18/cime/"+LastPostNum)
	    else:
		print("No data stored under this link")
		break

	    if(LastPostData.status_code == 200):
		print LastPostData.text
	    else:
	        print "Found the file link, but cant find the last post link..."	
		break


	else:
	    print "This link does not exsist"	
	    break

    if input_state == True and input_state!=OLDinput_state:
        GPIO.output(LedPin,False)


    OLDinput_state = input_state

