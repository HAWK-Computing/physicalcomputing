import machine
import time
from random import randint

Rot = machine.Pin(21, machine.Pin.OUT)
Gruen = machine.Pin(20, machine.Pin.OUT)

while True:
    TipTop = randint(0, 1)
    
    if (TipTop == 0):
        Rot.value(0)
        time.sleep(0.6)
        Rot.value(1)
        time.sleep(0.6)
    
    if (TipTop == 1):    
        Gruen.value(0)
        time.sleep(0.6)
        Gruen.value(1)
        time.sleep(0.6)
  #  time.sleep(0.6)

