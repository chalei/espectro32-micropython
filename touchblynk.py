'''using the capacitive touch sensor to trigger IO at blynk framework'''

import network
import socket
from machine import TouchPad, Pin
from time import sleep

touch = TouchPad(Pin(13))
led = Pin(15, Pin.OUT)


sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("ssid", "password")
sleep(4)

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()
	
while True:
    data = touch.read()
    if (data < 700):
      led.value(0)
      http_get('http://188.166.206.43/key/update/d4?value=1')
      sleep(4)
      http_get('http://188.166.206.43/key/update/d4?value=0')
      
    else:
      led.value(1)
  
	

