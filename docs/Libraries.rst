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

.. sourcecode::	led = machine.Pin(14, machine.Pin.OUT) # ohne Picozero Library
				led = LED(14) # mit Picozero Library

Befehle wie ``led.value(1)`` werden zu ``led.on()`` Noch nicht überzeugt? Wenn der Code komplexer wird und nicht nur mit LEDs gearbeitet wird, dann helfen die Vereinfachungen von picozero sehr effektiv!

Verwendung von Picozero
-----------------

Es kann genau das importiert werden, was gebraucht wird, indem die Einträge mit einem Komma getrennen werden``,``::

    from picozero import pico_led, LED

Dadurch können :obj:`~picozero.pico_led` und :class:`~picozero.LED` im Code verwendet werden::

    pico_led.on() # Turn on the LED on the Raspberry Pi Pico
    led = LED(14) # Control an LED connected to pin GP14 
    led.on()

.. _Picozero: https://picozero.readthedocs.io/en/latest/

.. note:: 
	Alle wichtigen **Anwendungsmöglichkeiten** von *picozero* in den `Rezepten <https://picozero.readthedocs.io/en/latest/recipes.html>`_ der sehr guten `Dokumentation <https://picozero.readthedocs.io/en/>`_

