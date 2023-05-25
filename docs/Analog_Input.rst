==========
Analoger Input
==========

Analog Inputs des Pi Pico
====================

Der Raspberry Pi Pico bestitzt **3 Analoge Eingänge**. Bzw. präziser müsste es heißen, dass an drei GPIO Pins durch einen integrierten 12bit *AnalogDigital Wandler* (auch ADC genannt) ein variabler Input möglich ist. 

.. warning:: 
	Was heißt das genau? Hier folgt eine genauere Erklärung in Kürze

Hardware Verkabelung
------------

Der Anschluss von Sensoren an den ADC Eingängen ist etwas komplizierter als das Anschließen eines Tasters. Bei einem **10k Poti** müssen die äußeren Beinchen jeweils an 3,3V und GROUND angeschlossen werden. Das mittlere Beinchen geht an den GPIO Pin 28 , 27 oder 26

.. literalinclude:: beispiele/Input_Analog_Poti.py

Der Code unter Verwendung der Picozero Library. Siehe dazu auch:
https://picozero.readthedocs.io/en/latest/recipes.html#potentiometer

Analoge Sensoren
-------------

LDR
Poti

