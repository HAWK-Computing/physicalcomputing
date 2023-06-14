'Quelle: https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html'
'einfacher Neopixel Code mit Taster der per Zufall die Farbe der LEDs ändert'
import machine, neopixel
import time
import random

np = neopixel.NeoPixel(machine.Pin(21), 8) #This configures a NeoPixel strip on GPIO4 with 8 pixels. You can adjust the “4” (pin number) and the “8” (number of pixel) to suit your set up.
taster=machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_UP)#Input
tasterWert = 0
r = 0
g = 0
b = 128

while True:
    
    n = np.n
    if taster.value() == 0:
        r = random.randint(0,128) # es gehen Werte von 0 bis 255
        g = random.randint(0,128)
        b = random.randint(0,128)
        print(r,g,b)
        
        for j in range(n):
            np[j] = (r, g, b)
            np.write()
            print(j)
            time.sleep_ms(150)
            
        for x in range(n-1, -1, -1):  #von n = Anzahl LedPixel bis 0
            np[x] = (0, 0, 0)
            print(x)
            np.write()
            time.sleep_ms(150)
