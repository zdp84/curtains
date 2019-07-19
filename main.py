#!/usr/bin/env python
import pigpio
import time
import sys

openPin = 17
closePin = 27


print('start')
pi = pigpio.pi()
pi.set_mode(openPin, pigpio.OUTPUT)
pi.set_mode(closePin, pigpio.OUTPUT)
pi.write(openPin,0)
pi.write(closePin,0)

if sys.argv[1] == 'open':
    pi.write(openPin,1)
    time.sleep(0.1)
    pi.write(openPin,0)
else:
    pi.write(closePin,1)
    time.sleep(0.1)
    pi.write(closePin,0)

print('stop')