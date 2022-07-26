pylev
=====

A pure Python Levenshtein implementation that's not freaking GPL'd.

Based off the Wikipedia code samples at
http://en.wikipedia.org/wiki/Levenshtein_distance.

.. image:: https://pepy.tech/badge/pylev
   :target: https://pepy.tech/project/pylev
.. image:: https://travis-ci.com/toastdriven/pylev.svg?branch=main
   :target: http://travis-ci.com/toastdriven/pylev
.. image:: https://img.shields.io/pypi/pyversions/pylev.svg?color=%2334D058?branch=main
   :target: https://pypi.org/project/pylev


Installation
------------

``pip install pylev``


Usage
-----

Usage is fairly straightforward:

.. code-block:: python

    import pylev
    distance = pylev.levenshtein('kitten', 'sitting')
    assert distance == 3


Tests
-----

Setup::

    $ git clone https://github.com/toastdriven/pylev.git
    $ cd pylev

Running::

    $ python -m unittest tests


Alternatives
------------

* https://pypi.org/project/levenshtein/ - GPL
* https://pypi.org/project/python-Levenshtein/ - GPL
* https://pypi.org/project/fuzzywuzzy/ - GPL
* https://pypi.org/project/pylevenshtein/ - GPL
* https://pypi.org/project/leven/ - Unknown license & requires Cython


Version History
---------------

* v1.5.0

    * Added an alternatives section. Thanks to @graingert for the start!

* v1.4.0

    * Updated for current versions of Python
    * Integrated a better Travis matrix. Thanks to @graingert!
    * Fixed mistaken docs about the `assert`. Thanks to @adamchainz!
    * Reorganized the package.
    * Blacked all the source code.

* v1.3.0

    * Implemented a considerably faster variants (orders of magnitude).
    * Tested & working on Python 2.7.4, Python 3.3.1 & PyPy 1.9.0.

* v1.2.0

    * Fixed all incorrect spellings of "Levenshtein" (there's no "c" in it).
    * Old methods are aliased for backward-compatibility.

* v1.1.0

    * Implemented a much faster variant (several orders of magnitude).
    * The older variant was renamed to ``classic_levenschtein``.
    * Tested & working on Python 3.3 & PyPy 1.6.0 as well.

* v1.0.2

    * Python packaging is **REALLY** hard. Including the README *this time*.

* v1.0.1

    * Python packaging is hard. Including the README this time.

* v1.0.0

    * Initial release, just the naive implementation of Levenshtein.


License
-------

New BSD.
