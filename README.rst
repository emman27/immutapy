[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Femman27%2Fimmutapy.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Femman27%2Fimmutapy?ref=badge_shield)

Immutapy - Immutable data structures for Python
===============================================

.. image:: https://travis-ci.org/emman27/immutapy.svg?branch=master
    :target: https://travis-ci.org/emman27/immutapy

.. image:: https://api.codacy.com/project/badge/Grade/5ccc6d4e7cf94c2ba1d7e24759852ae7
    :target: https://www.codacy.com/app/eygohlolz/immutapy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=emman27/immutapy&amp;utm_campaign=Badge_Grade

Immutapy is a library adding immutable data structures to Python to replace many of the standard
library data structures. This is inspired by immutable.js and caused by mutable data structures
generally just being a pain in the ass

Installing
----------

Immutapy can be installed from pip. Supported (tested) versions of Python are 2.7, 3.4, 3.5 and 3.6, although most modern versions should be fine.

.. code-block::

    pip install immutapy

Usage
-----

.. code-block:: python

    import immutable
    lst = immutable.List()
    new_list = lst.append(1)
    # >> lst == immutable.List()
    # True
    # >> new_list == immutable.List([1])
    # True

Features
--------

* ☐ Standard Library

  * ☑ List (Somewhat)
  * ☑ Dict
  * ☐ Set
* ☐ collections
* ☐ numpy

Performance Comparison
----------------------

Note that immutable structures tend to have a performance overhead.
Differences are highlighted in the table below.

Trivia: Python's standard library uses arrays to back lists.
See https://wiki.python.org/moin/TimeComplexity

==========  ========  =======================
Operation   List      immutable.List
lst.append  O(1)      O(n)
lst.pop()   O(1)      O(n)
lst.pop(i)  O(i)      O(n)
lst.extend  O(k)      O(n+k)
delete      O(n)      Not possible (immutable)
==========  ========  ========================


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Femman27%2Fimmutapy.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Femman27%2Fimmutapy?ref=badge_large)