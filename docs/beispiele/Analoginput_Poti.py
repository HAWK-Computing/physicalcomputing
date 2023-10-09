from machine import Pin, ADC
from time import sleep

potentiometer = ADC(28)


while True:
    poti_value = potentiometer.read_u16()
    print(poti_value)
    sleep(0.25)