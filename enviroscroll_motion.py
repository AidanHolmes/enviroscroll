# Enivro pHat and Scroll pHat Example for Python Copyright (C) 2017  Aidan Holmes
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# This example displays a dot which moves according to feedback
# from the enviro pHat accelerometer.
# The code calibrates from 30 readings and prints to stdout.

import sys
import time
from envirophat import light, weather, motion, analog, leds
import scrollphat

scrollphat.set_brightness(7)

# x, y, z min and max error calibrations
error = [[0,0], [0,0], [0,0]]
threshold = 0.2

def minmax(arr,x,y,z):
    if x < arr[0][0]: arr[0][0] = round(x,2)
    if x > arr[0][1]: arr[0][1] = round(x,2)
    if y < arr[1][0]: arr[1][0] = round(y,2)
    if y > arr[1][1]: arr[1][1] = round(y,2)
    if z < arr[2][0]: arr[2][0] = round(z,2)
    if z > arr[2][1]: arr[2][1] = round(z,2)

try:

    (x,y,z) = motion.accelerometer()
    error = [[x,x], [y,y], [z,z]]
    # Calibrate, assuming stationary
    for i in range(30):
        (x,y,z) = motion.accelerometer()
        minmax(error,x,y,z)
        time.sleep(0.1)
    print (error)
    print ("X range is {0}\nY range is {1}\nZ range is {2}".format(error[0][1]-error[0][0], error[1][1]-error[1][0], error[2][1]-error[2][0]))

    lastx = 0
    lasty = 0
    while True:
        
        (x,y,z) = motion.accelerometer()
        xg = 0
        yg = 0
        zg = 0

        if round(x,2) < error[0][0]: xg = error[0][0] - x
        if round(x,2) > error[0][1]: xg = error[0][1] - x 

        if round(y,2) < error[1][0]: yg = error[1][0] - y 
        if round(y,2) > error[1][1]: yg = error[1][1] - y

        if round(z,2) < error[2][0]: zg = error[2][0] - z
        if round(z,2) > error[2][1]: zg = error[2][1] - z

        xpos = int((xg * -1) / 0.1) + 5
        ypos = int(yg / 0.1) + 2
        zpos = int(zg / 0.1)

        if xpos > 10: xpos = 10
        if xpos < 0: xpos = 0
        if ypos > 4: ypos = 4
        if ypos < 0: ypos = 0

        if lastx != xpos or lasty != ypos:
            scrollphat.clear()
            scrollphat.set_pixel(xpos, ypos, 1)
            scrollphat.update()
            leds.on()

        lastx = xpos
        lasty = ypos
        
        time.sleep(0.1)
        leds.off()

except KeyboardInterrupt:
    scrollphat.clear()
                        
