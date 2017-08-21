'''
Menggunakan tombol A (Pin 0) atau B (Pin 4) sebagai inputan untuk menyalakan led (Pin 15)
'''


from machine import Pin
import time

button=Pin(4, Pin.IN) #Tombol B
led=Pin(15,Pin.OUT)   #Led Onboard

while True:
  led.value(button.value())
  time.sleep(0.1)
  print(button.value())
