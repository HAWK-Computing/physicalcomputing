import machine
import time
from random import randint

Rot = machine.Pin(21, machine.Pin.OUT)
Gruen = machine.Pin(20, machine.Pin.OUT)

while True:
    rotodergruen = randint(0, 1)
    
    if (rotodergruen == 0):
        Rot.value(0)
        time.sleep(0.6)
        Rot.value(1)
        time.sleep(0.6)
    
    if (rotodergruen == 1):    
        Gruen.value(0)
        time.sleep(0.6)
        Gruen.value(1)
        time.sleep(0.6)
 

