sensor-server
===============================

## Den Server automatisch on boot starten

- wir benutzen systemd: https://wiki.archlinux.de/title/Systemd
  - Damit kann unser Server als Systemweiter Service registriert werden

- Unter `/home/pi/`, Verzeichnis `sensor-server` erstellen und `app.py` reinkopieren
- Die Service-Datei `atmospace-server.service` in `/etc/systemd/system/` speichern
  - Die Datei beschreibt unseren Service: https://wiki.archlinux.de/title/Systemd/Eigener_Service
- Damit das System den neuen Service erkennt, Befehl `sudo systemctl daemon-reload` ausführen
  - Systemctl ist das System-Tool zur Administration und Prüfung der verwendeten Services
- Um den Service zu aktivieren und automatisch zu starten, `sudo systemctl enable atmospace-üserver.service` ausführen
- Der Server soll jetzt im port 5000 laufen
  - Service-Status überprüfen mit `sudo systemctl status atmospace-server.service`

### Service-Datei

```
[Unit]
Description=AtmoSpace Server
After=network.target

[Service]
Environment="FLASK_APP=/home/pi/sensor-server/app.py"
User=pi
Group=pi
ExecStart=/home/pi/.local/bin/flask run --host=0.0.0.0 --port=5000
Restart=always
RestartSec=2

[Install]
WantedBy=multi-user.target
```
