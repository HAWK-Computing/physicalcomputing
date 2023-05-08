"""Aufbau: Input Taster an Pin 21
            Output onboard LED Pin 25
"""
#Bibliotheken
import machine
import utime

led=machine.Pin(25, machine.Pin.OUT) #Output onboard LED
taster=machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)#Input 

while True:
    
    if taster.value() == 0: # da wir den Taster als PULL_UP Pin deklariert haben
                            # ist er immer 1 / HIGH / TRUE solange nicht gedrückt wird
        led.value(1)
        utime.sleep(0.5)  # kurze Pause, damit die LED nicht sofort ausgeht
    else:
        led.value(0)
    
