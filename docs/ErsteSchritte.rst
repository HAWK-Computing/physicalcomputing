Erste Schritte
=====

.. _installation:

Einrichten der Software
------------

Um mit dem Microcontroller Pi Pico arbeiten zu können, brauchen wir eine Entwicklungsumgebung (IDE) auf dem Computer. Zum Beispiel die `Thonny Python IDE`_
läuft auf Windows, Mac und Linux.

.. _Thonny Python IDE: https://thonny.org/

.. code-block:: console

   (.HAWKlocalmachine) $ pip install thonny


.. _pinout:

Das Pin Out des Raspberry Pi Pico
----------------

.. image:: bilder/PinBelegungPico.png
    :alt: Pinbelegung Raspberry Pi Pico.

.. literalinclude:: beispiele/HelloWorld.py

For example:

>>> import picozero
>>> # los geht's
['shells', 'gorgonzola', 'parsley']

.. _Steckbrett:

Das Steckbrett
-----------------

Schnell Prototyping mit dem Steckplatine auch genannt `Breadboard`_

.. _Breadboard: https://de.wikipedia.org/wiki/Steckplatine