==========
Vereinfachen mit Bibliotheken
==========

Mit sog. **Libraries** (auch **Bibliotheken** genannt) lässt sich Code auslagern. Warum das Rad neu erfinden, wenn es zu komplexen Anwendungen bereits Codebausteine gibt?

Verwendung von Libraries
==========

Indem wir die Library importieren, können wir die darin hinterlegten Befehle in unserem Code verwenden und ausführen.::

 	import machine			 # Import der kompletten Library
	from machine import Pin  # oder nur Teile daraus

Dokumentation zu der Library `machine`_ für den Raspberry Pi Pico 

.. _machine: https://docs.micropython.org/en/latest/rp2/quickref.html

Die Library Picozero
==========

Wie einfach die Programmierung und die Eingabe von Befehlen durch Libraries werden kann, zeigt die `Picozero`_ Library.


.. sourcecode::	led = machine.Pin(25, machine.Pin.OUT)
	led = LED(14) # Control an LED connected to pin GP14 

Komplizierte Befehle wie led.value(1) werden zu led.on() 

.. _Picozero: https://picozero.readthedocs.io/en/latest/

 
Anwendung der Library
------------

recepies
.. note::

.. sourcecode::

Wichtige Befehle
------------