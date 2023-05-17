# Code für den Anschluss von einem Potentiometer
# mit der Library picozero

from picozero import Pot, LED

# Potentiometer connected to GP26 (ADC0), GND and 3V
# LED connected to GP0

pot = Pot(26)
led =  LED(0)

while True:
    led.value = pot.value
    print(pot.value)
    