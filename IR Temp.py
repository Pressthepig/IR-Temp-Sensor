#  Designed specifically to work with the MLX90614 sensors in the
#  adafruit shop
#  ----> https://www.adafruit.com/product/1747
#  ----> https://www.adafruit.com/product/1748
#
#  These sensors use I2C to communicate, 2 pins are required to
#  interface Adafruit invests time and resources providing this open
#  source code,
#  please support Adafruit and open-source hardware by purchasing
#  products from Adafruit!

import time
import board
import busio
import adafruit_mlx90614
from adafruit_ht16k33 import segments
from adafruit_circuitplayground.express import cpx
import neopixel




# the mlx90614 must be run at 100k [normal speed]
# i2c default mode is is 400k [full speed]
# the mlx90614 will not appear at the default 400k speed
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)





# Basic example of setting digits on a LED segment display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain



# Import all board pins.

# Import the HT16K33 LED segment module.


# Create the I2C interface.


# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)
# Or this creates a 14 segment alphanumeric 4 character display:
# display = segments.Seg14x4(i2c)
# Or this creates a big 7 segment 4 character display
# display = segments.BigSeg7x4(i2c)
# Finally you can optionally specify a custom I2C address of the HT16k33 like:
# display = segments.Seg7x4(i2c, address=0x70)

# Clear the display.
display.fill(0)

display.colon = False


# temperature results in celsius
while True:

    IRtemp = ((mlx.object_temperature) * 1.8 + 32)

    if 0 <= IRtemp < 124:
        cpx.pixels.fill((0, 0, 255))
    elif 124 <= IRtemp < 188:
        cpx.pixels.fill((30, 30, 255))
    elif 188 <= IRtemp < 252:
        cpx.pixels.fill((61, 61, 255))
    elif 252 <= IRtemp < 316:
        cpx.pixels.fill((103, 103, 255))
    elif 316 <= IRtemp < 380:
        cpx.pixels.fill((150, 150, 255))
    elif 380 <= IRtemp < 444:
        cpx.pixels.fill((255, 255, 255))
    elif 444 <= IRtemp < 508:
        cpx.pixels.fill((255, 220, 220))
    elif 508 <= IRtemp < 572:
        cpx.pixels.fill((255, 120, 120))
    elif 572 <= IRtemp < 636:
        cpx.pixels.fill((255, 60, 60))
    elif 636 <= IRtemp < 700:
        cpx.pixels.fill((255, 30, 30))
    elif IRtemp >= 700:
        cpx.pixels.fill((255, 0, 0))




    print("IR Temp: ", IRtemp)
    display.print("% 5.1f" % IRtemp)
    time.sleep(0.1)
