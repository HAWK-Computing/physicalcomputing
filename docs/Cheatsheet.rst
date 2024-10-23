Cheatsheet MicroPython
=========


.. note:: Ein kleines *Glossar / Nachschlageseite* zu den wichtigsten Befehlen von Micropython. Diese Sammlung wird stetig ergänzt und erweitert. tba.



Programm Basics
-----------------------

**Kommentare** helfen dabei sich im Code zurecht zu finden oder bestimmte Codeschnipsel vorübergehend zu deaktivieren ohne sie löschen.
.. sourcecode:: 
 # this is a simple comment, in only one line
 """ this is a multi line comment 
 	 to describe some more details """

**Bedingung / Conditions** kleiner Ausschnitt (tbc)

.. sourcecode::
	if a == b:				# wenn a gleich b ist dann:
		tue_etwas()	
	if a > b:				# wenn a größer b ist dann:
    	tue_dies() 			
   	if a < b:				# wenn a kleiner b ist dann:
   		tue_das()

   	if a == b and b > c:	# wenn a gleich b ist UND b größer c dann:
   		tue_alles()
   	if a == b or b > c:		# wenn entweder a gleich b ist ODER b größer c dann:
   		tue_beides()

   		
*siehe dazu auch: https://www.w3schools.com/python/python_conditions.asp

**Schleife**

>>> for i in range (Startzahl, Endzahl, Schrittzahl):

**Funktionen im Zusammenhang mit der Hardware**

.. sourcecode:: 
	import machine

	machine.Pin.OUT
	machine.reset() # Setzt das Gerät auf ähnliche Weise zurück wie das Drücken 				# der externen RESET-Taste.
	

**Interessante Python Beispiele**

https://www.python-lernen.de/if-abfrage-python.htm
https://pythonexamples.org/python-for-i-in-range/
https://realpython.com/python-and-operator/
https://problemsolvingwithpython.com/04-Data-Types-and-Variables/04.02-Boolean-Data-Type