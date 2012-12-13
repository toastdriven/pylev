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

"""
__author__ = 'Daniel Lindsley'
__version__ = (1, 1, 0)
__license__ = 'New BSD'


def classic_levenschtein(string_1, string_2):
    """
    Calculates the Levenschtein distance between two strings.

    This version is easier to read, but significantly slower than the version
    below (up to several orders of magnitude). Useful for learning, less so
    otherwise.

    Usage::

        >>> classic_levenschtein('kitten', 'sitting')
        3
        >>> classic_levenschtein('kitten', 'kitten')
        0
        >>> classic_levenschtein('', '')
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
            classic_levenschtein(string_1[1:], string_2) + 1,
            classic_levenschtein(string_1, string_2[1:]) + 1,
            classic_levenschtein(string_1[1:], string_2[1:]) + cost,
        )


def levenschtein(string_1, string_2, len_1=None, len_2=None, offset_1=0, offset_2=0, memo=None):
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
    if len_1 is None:
        len_1 = len(string_1)

    if len_2 is None:
        len_2 = len(string_2)

    if memo is None:
        memo = {}

    key = ','.join([str(offset_1), str(len_1), str(offset_2), str(len_2)])

    if memo.get(key) is not None:
        return memo[key]

    if len_1 == 0:
        return len_2
    elif len_2 == 0:
        return len_1

    cost = 0

    if string_1[offset_1] != string_2[offset_2]:
        cost = 1

    dist = min(
        levenschtein(string_1, string_2, len_1 - 1, len_2, offset_1 + 1, offset_2, memo) + 1,
        levenschtein(string_1, string_2, len_1, len_2 - 1, offset_1, offset_2 + 1, memo) + 1,
        levenschtein(string_1, string_2, len_1 - 1, len_2 - 1, offset_1 + 1, offset_2 + 1, memo) + cost,
    )
    memo[key] = dist
    return dist
