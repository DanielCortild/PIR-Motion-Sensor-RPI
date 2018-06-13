import time
import os
import psutil
import grovepi
pir_sensor = 8

grovepi.pinMode(pir_sensor,"INPUT")

while True:
    try:
        if grovepi.digitalRead(pir_sensor):
            print("Mouvement")
        else:
			print("-")
        time.sleep(.2)

    except IOError:
        print "Error"
