#Aufbau: Input auslesen und Led steuern

#Bibliotheken
import machine
import utime

#Was brauchen wir dafür?
#Variablen 
Pin-Nummer = 15
#Variablen und wo und was sie machen
led=machine.Pin(25, machine.Pin.OUT) #Output
taster=machine.Pin(Pin-Nummer, machine.Pin.IN, Pull_UP)#Input

while True:
    if taster.value() == 1:
        led.value(1)
        utime.sleep(0.1)
    led.value(0)    
    

