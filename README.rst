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

Usage is fairly straightforward.::

    import pylev
    distance = pylev.levenshtein('kitten', 'sitting')
    assert(distance, 3)


License
-------

New BSD.


Tests
-----

Setup::

    $ git clone https://github.com/toastdriven/pylev.git
    $ cd pylev
    $ virtualenv env --distribute
    $ . env/bin/activate
    $ pip install unittest2

Running::

    $ python -m unittest2 tests


Version History
---------------

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