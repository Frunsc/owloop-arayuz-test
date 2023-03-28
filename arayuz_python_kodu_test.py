import rp2
import network
import ubinascii
import machine
import urequests as requests
import time
import socket
import json
from machine import ADC
from time import sleep
import _thread
import random

ssid = "SUPERONLINE_WiFi_5521"
pw = "ZcCkeNHY2eAC"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(pm = 0xa11140)

wlan.connect(ssid, pw)
running = False

light = machine.Pin("LED", machine.Pin.OUT)
sensor_temp = ADC(4)
conv_factor = 3.3 / (65535)
LED= machine.Pin(13,machine.Pin.OUT)


timeout = 10
while timeout > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    timeout -= 1
    print('Waiting for connection...')
    time.sleep(1)
    
  
def blink_onboard_led(num_blinks):
    led = machine.Pin('LED', machine.Pin.OUT)
    for i in range(num_blinks):
        led.on()
        time.sleep(.2)
        led.off()
        time.sleep(.2)
    

wlan_status = wlan.status()
blink_onboard_led(wlan_status)

if (wlan_status != 3 or timeout==0):
    print('Wi-Fi connection failed')
    machine.reset()
else:
    print('Connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])
    


print(wlan.ifconfig())
addr = ('', 80)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen(1)

print('Listening on', addr)
led = machine.Pin('LED', machine.Pin.OUT)

while True:   
    cl, addr = s.accept()
    print('Client connected from', addr)
    r = cl.recv(2048).decode()
    r = str(r)
    print(r)
    if r=='connected':
        break

running = False
def temp():
    basinc=0
    t=0
    konum=0
    hiz=0
    ivme=0
    
    while running:
        reading = sensor_temp.read_u16() * conv_factor
        temperature = 27 - (reading - 0.706)/0.001721
        temp_as_str = str(temperature)
        print(temperature)
        time.sleep(0.1)
        #random
        basinc= random.uniform(1,1.5)
        t+=1
        hiz = 1*t
        konum += hiz*1
        ivme = 1

        

        
        veriler= {"sicaklik":temperature, "hiz":hiz, "basinc":basinc, "konum":konum, "ivme":ivme}
        data= json.dumps(veriler)
        data = str(data)
        cl.send(data.encode())
        
        


while True:
    try:
        r = cl.recv(2048).decode()
        r = str(r)
        
        print(r)
        

        
        if r == 'ledac':
            led.value(1)
            LED.value(1)
            running = True
        if r == 'ledkapat':
            led.value(0)
            LED.value(0)
            running = True
            
        if r== 'baslat':
            running= True
            _thread.start_new_thread(temp, ())
        
        if r== 'durdur':
            running = False
            
        if r=='baglantiyi_kes':
            machine.reset()
        
    except KeyboardInterrupt:
        machine.reset()
    except OSError as e:
        cl.close()
        print('Connection closed')
        machine.reset()
        
        
        
        
        



