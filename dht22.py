from machine import Pin
import time
import dht

sensor = dht.DHT22Pin(26))

delay = 2


while True:
  try:
    sensor.measure()
    print(sensor.temperature(), "C")
    print(sensor.humidity(), "persen")

    time.sleep(delay)
  except OSError:
     pass
          
