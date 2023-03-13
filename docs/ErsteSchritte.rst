Erste Schritte
=====

.. _installation:

Einrichten der Software
------------

Um mit dem Microcontroller Pi Pico arbeiten zu können, brauchen wir eine Entwicklungsumgebung (IDE) auf dem Computer:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:


.. image:: bilder/PinBelegungPico.png
    :alt: Pinbelegung Raspberry Pi Pico.

.. literalinclude:: beispiele/HelloWorld.py

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

