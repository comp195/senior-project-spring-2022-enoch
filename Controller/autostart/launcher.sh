#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/pygame/Enoch_Controller
qjoypad "controller" &
sudo python3 menu.py
while True:
do
	sleep(99999)
done
