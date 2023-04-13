Der Raspberry Pi Pico
===============

Das Pin Out des Raspberry Pi Pico
----------------
.. _pinout:
.. image:: bilder/PinBelegungPico.png
    :alt: Pinbelegung Raspberry Pi Pico


Der RP2040 Chip
-----------------

Der `RP2040`_ Chip von der Raspberry Pi Foundation 2021 entworfen und entwickelt, bildet das Herzstück für den Raspberry Pi Pico Microcontroller.

.. _RP2040: https://de.wikipedia.org/wiki/RP2040

   
+------------------------+----------------------------------+
| Bezeichnung            | Spezifikation                    |
+========================+==================================+
| Prozessor              | Zwei Kerne Arm Cortex M0+        |
+------------------------+----------------------------------+
| Taktfrequenz           | bis zu 133 MHz                   |
+------------------------+----------------------------------+
| Flashspeicher          | 264 kB SRAM                      |
|                        | 2 MB on-board Flashspeicher      |
+------------------------+----------------------------------+
| Input/Output Pins      | 26 × GPIO Pins                   |
|                        | 2 × SPI, 2 × I2C, 2 × UART       |    
|                        | 3 × 12-bit ADC (Analog Digital Wandler)|
+------------------------+----------------------------------+
| Stromversorgung        | Spannung Input 2-5,5 V DC        |
+------------------------+----------------------------------+
| Arbeitsspannung        | 3,3 Volt max 10mA pro GPIO Pin   |
+------------------------+----------------------------------+ 
| Besonderheiten         | Temperatursensor, onBoard LED,   |
|                        | Debugging Schnittstelle          |
+------------------------+----------------------------------+          
   

.. note:: siehe dazu auch die ausführliche Beschreibung im Elektronik Kompendium zum Thema `Raspberry Pi Pico <https://www.elektronik-kompendium.de/sites/raspberry-pi/2604131.htm>`_


.. image:: bilder/RaspberryPiPico_Steckbrett_Kabel.png
    :alt: Startset des Raspberry Pi Pico


