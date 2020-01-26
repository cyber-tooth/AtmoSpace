import requests
import time
import board
import busio
import adafruit_dht
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

#create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

#create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

#create single-ended input on channels
chan0 = AnalogIn(ads, ADS.P0)


#define frequency of measurements
delayTime = 5

#Initial dht device with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)
pin=4

GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_OFF)
while True:

 global loud
 global temp
 global hum

 loud='%.2f' % chan0.value
 temp= dhtDevice.temperature
 hum=dhtDevice.humidity

 print ("Loudness:", loud)
 print ("Temp: {:.1f}*C  Humidity:{}%" .format(temp,hum))
 print ("_______________________________________________________")
 time.sleep(delayTime)

 url = "http://thoughtworks.f4.htw-berlin.de/var/www/html/submitdata.php"

 payload = {'temperature':temp, 'humidity': hum, 'loudness': loud}
 r = requests.post(url,data = payload)
 print (r.text)
