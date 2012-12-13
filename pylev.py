"""
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
"""
__author__ = 'Daniel Lindsley'
__version__ = (1, 0, 2)
__license__ = 'New BSD'


def levenschtein(string_1, string_2):
    """
    Calculates the Levenschtein distance between two strings.

    Usage::

        >>> levenschtein('kitten', 'sitting')
        3
        >>> levenschtein('kitten', 'kitten')
        0
        >>> levenschtein('', '')
        0

    """
    len_1 = len(string_1)
    len_2 = len(string_2)
    cost = 0

    if len_1 and len_2 and string_1[0] != string_2[0]:
        cost = 1

    if len_1 == 0:
        return len_2
    elif len_2 == 0:
        return len_1
    else:
        return min(
            levenschtein(string_1[1:], string_2) + 1,
            levenschtein(string_1, string_2[1:]) + 1,
            levenschtein(string_1[1:], string_2[1:]) + cost,
        )
