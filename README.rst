pylev
=====

A pure Python Levenschtein implementation that's not freaking GPL'd.

Based off the Wikipedia code samples at
http://en.wikipedia.org/wiki/Levenshtein_distance.

Usage
-----

Usage is fairly straightforward.::

    import pylev
    distance = pylev.levenschtein('kitten', 'sitting')
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

* v1.0.2

    * Python packaging is **REALLY** hard. Including the README *this time*.

* v1.0.1

    * Python packaging is hard. Including the README this time.

* v1.0.0

    * Initial release, just the naive implementation of Levenschtein.