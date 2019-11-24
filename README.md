# AtmoSpace

## Daten schlicht durch Apache darstellen:

Zuerst habe ich auf meinem Raspberry Pi einen Apache Web Server installiert via dem Befehl:

$ sudo apt install apache2

Danach habe ich den Webserver neu gestartet, damit er laeuft:

$ sudo service apache2 restart

Jetzt kann ich auf meinem Laptop die IP-Adresse des Raspberrys eingeben und sehe eine index.html Seite, die auf meinem Raspberry im Verzeichnis /var/www/html liegt.

Ich muechte aber, dass auf dieser Seite die Werte erscheinen die mein DHT11-Sensor an Raumtemperatur und Raumluftfeuchtigkeit misst, dargestellt werden. 

Dafuer schreibe ich ein Python-Skript, das die Werte liest (siehe die Datei simpletest.py)

Dann erstelle ich einen neue index-Datei im Raspberry-Verzeichnis /var/www/html namens Index.php (siehe Datei im Repo). Damit diese angesprochen wird, muss die alte index.html-Datei im Verzeichnis geloescht werden.

Nun muss dem Nutzer www-data, der für den Webserver zuständig ist, das Recht gegeben werden, dieses Skript mit sudo auszuführen. Dafür schreiben wir in der Datei 010_pi-nopasswd 1 Zeile:
$ sudo nano /etc/sudoers.d/010_pi-nopasswd 

www-data ALL=NOPASSWD: /home/pi/simpletest.py

Dann machen wir die Skript-Datei für den Nutzer auch noch lesbar und ausführbar mit folgenden Befehlen in dem Verzeichnis indem sich die Skriptdatei befindet:
$ sudo chown pi:pi simpletest.py 
$ chmod +x simpletest.py 
$ ls -l simpletest.py 

Jetzt im Browser IP des Raspis angeben. Bei Refresh kommen die neuen Werte rein.
