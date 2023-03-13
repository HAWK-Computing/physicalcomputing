#Rundenzaehler

import machine
import utime

runden = 0 #Variable mit dem Namen: runden

#Loop
while True:
    print("Runden:" , runden)
    runden=runden+1 
    utime.sleep(1)
