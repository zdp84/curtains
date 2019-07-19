# curtains/main.yp

Automatic curtains opener.

# sudo nano /etc/rc.local
# pigpio daemon for GPIO Python usage.
sudo pigpiod &


crontab -e
# m h  dom mon dow   command
0 22 * * * python3 /home/pi/curtains/main.py close
30 5 * * * python3 /home/pi/curtains/main.py open
