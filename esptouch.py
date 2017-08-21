'''ini adalah sampel koding untuk capacitive touch sensor pada esp32'''


from machine import TouchPad, Pin
from time import sleep

touch = TouchPad(Pin(2)) #Tombol A pada espectro board
led = Pin(15, Pin.OUT) #onboard LED



while True:
    data = touch.read()
    print(data)
    if (data < 700):
      led.value(0)
      
    else:
      led.value(1)
  
	

