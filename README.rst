Immutapy - Immutable data structures for Python
===================================================

.. image:: https://travis-ci.org/emman27/immutablepy.svg?branch=master
    :target: https://travis-ci.org/emman27/immutablepy

.. image:: https://api.codacy.com/project/badge/Grade/a547e928fd994048aa9b63686b0557af
    :target: https://www.codacy.com/app/eygohlolz/immutablepy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=emman27/immutablepy&amp;utm_campaign=Badge_Grade

Installing: Immutapy can be installed from pip. Supported (tested) versions of Python are 2.7, 3.4, 3.5 and 3.6, although most modern versions should be fine.

.. code-block::

    pip install immutapy


Immutapy is a library adding immutable data structures to Python to replace many of the standard
library data structures. This is inspired by immutable.js and caused by mutable data structures
generally just being a pain in the ass

Usage:

.. code-block:: python

    import immutable
    lst = immutable.List()
    new_list = lst.append(1)
    # >> lst == immutable.List()
    # True
    # >> new_list == immutable.List([1])
    # True
