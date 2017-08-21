from machine import TouchPad, Pin, I2C
from time import sleep

import ssd1306

touch = TouchPad(Pin(4))
led = Pin(16, Pin.OUT)

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)

lcd=ssd1306.SSD1306_I2C(128,64,i2c)
lcd.text("Test",0,0)
lcd.text("TouchPad",24,16)
lcd.text("ESP32",64,24)
lcd.show()

while True:
  data = touch.read()
  lcd.fill(0)
  lcd.text("TouchPad", 0,0)
  lcd.text("Value is:", 0,16)
  lcd.text(str(data),72,16)
  lcd.show()
  print(data)
  sleep(0.5)


