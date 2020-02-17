# AtmoSpace

The AtmoSpace project provides an office space monitoring station that monitors, records and displays the temperature, humidity and loudness in an office. 
The architecture of the AtmoSpace monitoring station is as follows
![AtmoSpace Architecture](https://github.com/cyber-tooth/AtmoSpace/blob/master/ArchDiagram.png)
## Raspberry Pi and Sensor Setup
The left-hand side depicts a Raspberry Pi with 2 sensors attached and a Python script. The Python script reads the sensor data and sends it to a php-script running on a web server. The sensors that were used in this case were the DHT11 for temperature and humidity and the Grove loudness sensor. The Grove loudness sensor also requires an analog-digital converter.
The Python script is directly available in the AtmoSpace repository as [sensorData.py](https://github.com/cyber-tooth/AtmoSpace/blob/master/sensorData.py).
### Webserver Setup
