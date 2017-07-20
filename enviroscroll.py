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
# This example displays pressure, temperature and heading
# onto the scroll pHat display using Pimoroni Python libraries

import sys
import time
import select

from envirophat import light, weather, motion, analog
import scrollphat

scrollphat.set_brightness(7)

print ("Press Return key to change display")

mode = 0

while True:
    
    try:
        f = select.select([sys.stdin], [], [], 0)[0]
        if len(f) > 0:
            f[0].readline()
            mode += 1
            if mode > 2: mode = 0
            print ("Changing mode to {}".format(mode))
            scrollphat.clear()
            scrollphat.scroll_to(0)
            

        if mode == 0:
            scrollphat.scroll()
            scrollphat.write_string("{0:2.0f}C  ".format(weather.temperature()))
        elif mode == 1:
            scrollphat.scroll()
            scrollphat.write_string("{0:.2f}hPa  ".format(weather.pressure()))
        elif mode == 2:
            scrollphat.scroll(0)
            scrollphat.write_string("{0:3.0f} ".format(motion.heading()))
        else:
            scrollphat.write_string("No mode  ")
    
            
        time.sleep(0.35)
    except KeyboardInterrupt:
        scrollphat.clear()
        break
                        
