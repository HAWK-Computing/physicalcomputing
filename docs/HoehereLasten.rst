==========
Höhere Lasten
==========

.. warning:: 
	Achtung! Hier wird mit externen Stromquellen gearbeitet. Bei falscher Verkabelung, kann das zur **Zerstörung** des Microcontrollers oder auch eines daran (per USB Kabel) angeschlossenen Computers führen!!!

Elektronischer Background
------------
Wie können wir höhere Ströme und Verbraucher mit einem Microcontroller steuern. Dazu braucht es weitere Bauteile. Es geht um die Trennung von *Steuer*- und *Arbeitsstromkreis*. Dabei hilft ein sog. Optokoppler. Zum Beispiel ein 4N35:

.. image:: bilder/4n35.jpg

Dieses Bauteil trennt zwei Stromkreise voneinander indem es Signal mit Hilfe von Licht (LED) an einen Fototransistor weitergibt. 

Als Verstärkung oder Schalter kann dann zum Beispiel ein TIP 120 Transistor verwendet werden. 

.. image:: bilder/TIP120.jpg

Ein `MOSFET <https://www.youtube.com/watch?v=JTFTsVKR_00>`_ funktioniert ähnlich. 

Der Vorteil gegenüber einem Relais ist, dass auch PWM Signale verarbeitet werden können. Da die Reaktionszeit eines Transistors viel schneller sind. Somit ist das Dimmen von LEDs oder das Regeln von Geschwindigkeiten bei Motoren damit möglich. 



Shield vs. Selber bauen
------------
HW-532

.. image:: bilder/HW-532_Closeup.jpg


Relais Shield

.. image:: bilder/Relais_shield.jpg


Aufbau der Schaltung
-------------

https://www.youtube.com/watch?v=eqXaqRFAWrA


