# AtmoSpace

The AtmoSpace project provides an office space monitoring station that monitors, records and displays the temperature, humidity and loudness in an office. 
This repository contains files and folders that are not necessary for running the system. These files and folders were part of our learning and exploratory process and serve to depict this process and help others who wish to explore the setup further.
The architecture of the AtmoSpace monitoring station is as follows
![AtmoSpace Architecture](https://github.com/cyber-tooth/AtmoSpace/blob/master/ArchDiagram.png)
## Raspberry Pi and Sensor Setup
The left-hand side depicts a Raspberry Pi with 2 sensors attached and a Python script. The Python script reads the sensor data and sends it to a php-script running on a web server. The sensors that were used in this case were the DHT11 for temperature and humidity and the Grove loudness sensor. The Grove loudness sensor also requires an analog-digital converter.
The Python script is directly available in the AtmoSpace repository as [sensorData.py](https://github.com/cyber-tooth/AtmoSpace/blob/master/sensorData.py).
## Webserver Setup
For AtmoSpace, the webserver was used to contain an SQL database, a PHP-script for receiving data from the Raspberry Pi and writing it into the database, a PHP-script for reading the most recent data received, and a landingpage that will display the data by calling the PHP-script that reads this data from the database.
The webserver setup will go into installing the webserver, making sure that the correct landingpage is displayed, setting up an SQL database on the webserver and securing the webserver.
### Basic Webserver Setup
Login to the server to be used as webserver. Install Apache2 using the command `$ sudo apt install apache2`.
### Basic SQL Database Setup

### Create Landingpage and PHP-Skripts for Database Communication

`$ sudo apt install php-mysql`

### Secure Apache Webserver
To ensure that only encrypted communication is allowed with the server via SSL, create and install a certificate on the server. You may also want to redirect HTTP port 80 to HTTPS port 443.
In order to create and install a certificate use the command ...
