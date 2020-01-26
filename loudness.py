#Adapted from code by Adafruit Company, Joy-IT and Tony DiCola
#Author: Nyx Nyschd

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

#create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

#create single-ended input on channels
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

#define frequency of measurements
delayTime = 5

#optional: define digital-PIN on Pi:
Digital_PIN = 24

GPIO.setup(Digital_PIN, GPIO.IN, pull_up_down = GPIO.PUD_OFF)
while True:

 global loudness
 loudness='%.2f' % chan0.value

 print ("ADC-value:", loudness,)

 print("_________________________________________________")


 #reset und delay
 button_pressed = False
 time.sleep(delayTime)

