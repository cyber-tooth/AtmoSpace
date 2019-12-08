#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys
from flask import Flask, jsonify,render_template
import Adafruit_DHT

app = Flask(__name__)

@app.route("/lp1")
def home():
    return render_template("index.html")

@app.route("/lp2")
def lp2():
    return render_template("lp2.html")

@app.route("/")
def get_sensor_data():
    sensor = 11
    pin = 4
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Un-comment the line below to convert the temperature to Fahrenheit.
    # temperature = temperature * 9/5.0 + 32

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        return jsonify({'temp': temperature, 'hum': humidity})
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)

@app.route("/lp2-data")
def get_sensor_data_for_lp():
    sensor = 11
    pin = 4
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Un-comment the line below to convert the temperature to Fahrenheit.
    # temperature = temperature * 9/5.0 + 32

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        return render_template("lp2.html", temperature = temperature, humidity= humidity )
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)

@app.route("/temperature")
def get_sensor_temp():
    sensor = 11
    pin = 4

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if temperature is not None:

        return jsonify({'temperature': temperature})
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)

@app.route("/humidity")
def get_sensor_humidity():
    sensor = 11
    pin = 4

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None:

        return jsonify({'humidity': humidity})
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)

if __name__ == '__main__':
    app.run(debug=True)
