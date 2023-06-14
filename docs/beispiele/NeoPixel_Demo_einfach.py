'Quelle: https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html'
'Lauflicht auf und ab ohne Taster'

import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(21), 8) #This configures a NeoPixel strip on GPIO4 with 8 pixels. You can adjust the “4” (pin number) and the “8” (number of pixel) to suit your set up.

while True:
    
    n = np.n
       
    for j in range(n):
        np[j] = (0, 0, 128)
        np.write()
        print(j)
        time.sleep_ms(150)
        
    for x in range(n-1, -1, -1):  #von n = Anzahl LedPixel bis 0
        np[x] = (0, 0, 0)
        print(x)
        np.write()
        time.sleep_ms(150)