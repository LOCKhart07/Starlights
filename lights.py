from RPiSim.GPIO import GPIO
#import RPi.GPIO as GPIO
import time
import pyrebase
import re
import pickle
from datetime import datetime,timedelta

# Set Parameters
ledOn=GPIO.LOW
ledOff=GPIO.HIGH

# Check Input change
def checkData():
    try:
        rtd = open('datafile.pickle', 'rb')
        params = pickle.load(rtd)
        tempTime = params['TimeDelay']
        timeSplice = re.findall(r"[-+]?\d*\.\d+|\d+", str(tempTime))
        tempAuto = params['autoDelay']
        autoSplice = re.findall(r"[-+]?\d*\.\d+|\d+", str(tempAuto))
        global seq
        seq = int(params['sequenceNo'])
        global timeDelay
        try:
            timeDelay = float(timeSplice[0])
        except:
            timeDelay = 0.7
        global autoDelay
        try:
            autoDelay = int(float(autoSplice[0])*60)
        except:
            autoDelay=300
        rtd.close()
    except:
        print("Could not retrieve the parameters")
    print("Sequence No:",seq)
    print("Time Delay:",timeDelay)
    print("autodelay: ",autoDelay)

# Sequence Chooser
def sequenceChooser():
    while True:
        checkData()
        
        if(seq==1):
            sequence1(timeDelay) 
        elif(seq==2):
            sequence2(timeDelay)
        elif(seq==3):
            sequence3(timeDelay)
        elif(seq==4):
            sequence4(timeDelay)
        elif(seq==5):
            sequence5(timeDelay)
        elif(seq==6):
            sequence6()
        elif(seq==7):
            sequence7(timeDelay)
        else:
            print("Invalid sequence number")

# Sequences
def sequence1(timeDelay):
    for led in leds:
        print(led)
        GPIO.output(led,ledOn)
        time.sleep(timeDelay)
        GPIO.output(led,ledOff)
        
    print("All on")
    for led in leds:
        GPIO.output(led,ledOn)
    time.sleep(timeDelay)
    print("All off\n")
    for led in leds:
        GPIO.output(led,ledOff)

def sequence2(timeDelay):
    for led in leds:
        print(led)
        GPIO.output(led,ledOn)
        time.sleep(timeDelay)
        GPIO.output(led,ledOff)
        
    print("All on")
    for led in leds:
        GPIO.output(led,ledOn)
    time.sleep(timeDelay)
    print("All off\n")
    for led in leds:
        GPIO.output(led,ledOff)

    for led in reversed(leds):
        print(led)
        GPIO.output(led,ledOn)
        time.sleep(timeDelay)
        GPIO.output(led,ledOff)

    print("All on")
    for led in leds:
        GPIO.output(led,ledOn)
    time.sleep(timeDelay)
    print("All off\n")
    for led in leds:
        GPIO.output(led,ledOff)

def sequence3(timeDelay):
    print("All on")
    for led in leds:
        GPIO.output(led,ledOn)
    time.sleep(timeDelay)
    print("All off\n")
    for led in leds:
        GPIO.output(led,ledOff)
    time.sleep(timeDelay)

def sequence4(timeDelay):
    print(leds[0])
    GPIO.output(leds[0],ledOn)
    time.sleep(timeDelay)

    print(leds[1])
    GPIO.output(leds[1],ledOn)
    print(leds[4])
    GPIO.output(leds[4],ledOn)
    time.sleep(timeDelay)

    print(leds[2])
    GPIO.output(leds[2],ledOn)
    print(leds[3])
    GPIO.output(leds[3],ledOn)
    time.sleep(timeDelay)

    print("All off\n")
    for led in leds:
        GPIO.output(led,ledOff)
    time.sleep(timeDelay)

def sequence5(timeDelay):
    for led in leds:
        print(led)
        GPIO.output(led,ledOn)
        time.sleep(timeDelay)
    for led in leds:
        GPIO.output(led,ledOff)
    time.sleep(timeDelay)

def sequence6():
    print("All on")
    for led in leds:
        GPIO.output(led,ledOn)

def sequence7(timeDelay):
    timex=datetime.now()
    timey=timex+timedelta(seconds=+autoDelay)
    while timex<timey :
        timex=datetime.now()
        sequence1(timeDelay)
        checkData()
        if seq!=7 :
            break
    timex=datetime.now()
    timey=timex+timedelta(seconds=+autoDelay)
    while timex<timey :
        timex=datetime.now()
        sequence2(timeDelay)
        checkData()
        if seq!=7 :
            break
    timex=datetime.now()
    timey=timex+timedelta(seconds=+autoDelay)
    while timex<timey :
        timex=datetime.now()
        sequence3(timeDelay)
        checkData()
        if seq!=7 :
            break
    timex=datetime.now()
    timey=timex+timedelta(seconds=+autoDelay)
    while timex<timey :
        timex=datetime.now()
        sequence4(timeDelay)
        checkData()
        if seq!=7 :
            break
    timex=datetime.now()
    timey=timex+timedelta(seconds=+autoDelay)
    while timex<timey :
        timex=datetime.now()
        sequence5(timeDelay)
        checkData()
        if seq!=7 :
            break

# Intitalize leds 
leds=[13,19,26,16,20]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for led in leds:
    GPIO.setup(led,GPIO.OUT)
print("LEDs initialized")

# Testing leds
for led in leds:
    GPIO.output(led,ledOn)
time.sleep(1)
for led in leds:
    GPIO.output(led,ledOff)
print("LEDs tested \n")

# Go to sequence chooser
sequenceChooser()
print("Sequence ",seq," selected")