pylev
=====

A pure Python Levenshtein implementation that's not freaking GPL'd.

Based off the Wikipedia code samples at
http://en.wikipedia.org/wiki/Levenshtein_distance.


Requirements
------------

* Python 2.7.X, Python 3.3+ or PyPy 1.6.0+


Usage
-----

Usage is fairly straightforward:

.. code-block:: python

    import pylev
    distance = pylev.levenshtein('kitten', 'sitting')
    assert distance == 3


License
-------

New BSD.


Tests
-----

Setup::

    $ git clone https://github.com/toastdriven/pylev.git
    $ cd pylev

Running::

    $ python -m unittest tests

.. image:: https://travis-ci.com/toastdriven/pylev.svg?branch=main
   :target: http://travis-ci.com/toastdriven/pylev


See also
--------

* https://pypi.org/project/python-Levenshtein/ freaking GPL'd
* https://pypi.org/project/fuzzywuzzy/ freaking GPL'd by accident
* https://github.com/maxbachmann/RapidFuzz fork of the above before they accidently GPL'd it

Version History
---------------

* v1.4.0

    * Updated for current versions of Python
    * Integrated a better Travis matrix. Thanks to @grainert!
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
