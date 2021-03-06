from machine import Pin
from time import sleep
import neopixel

pin = Pin(27, Pin.OUT)
npix = neopixel.NeoPixel(pin, 1)

def LightAll(col):
    for pix in range(0, 1):
        npix[pix] = col
    npix.write()
    return

while True:
   for i in range(0,255,5):
       LightAll((0,i,0))
       sleep(0.02)
   for i in range(255,-1,-5):
       LightAll((0,i,0))
       sleep(0.02)
   for i in range(0,255,5):
       LightAll((0,0,i))
       sleep(0.02)
   for i in range(255,-1,-5):
       LightAll((0,0,i))
       sleep(0.02)
   for i in range(0,255,5):
       LightAll((i,0,0))
       sleep(0.02)
   for i in range(255,-1,-5):
       LightAll((i,0,0))
       sleep(0.02)
