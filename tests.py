import itertools
import unittest
import pylev

test_data = [
    ('classic', "kitten", "sitting", 3),
    ('same', "kitten", "kitten", 0),
    ('empty', "", "", 0),
    ('a', "meilenstein", "levenshtein", 4),
    ('b', "levenshtein", "frankenstein", 6),
    ('c', "confide", "deceit", 6),
    ('d', "CUNsperrICY", "conspiracy", 8),
]

test_functions = [
    # pylev.classic_levenshtein,   # disabled because it is so slow
    pylev.recursive_levenshtein,
    pylev.wf_levenshtein,
    pylev.wfi_levenshtein
]

class Tests(unittest.TestCase):

    pass


def _mk_test_fn(fn, a, b, expected):
    return lambda self: self.assertEqual(fn(a, b), expected)


for lev_fn, data in itertools.product(test_functions, test_data):
    name, a, b, expected = data
    test_fn = _mk_test_fn(lev_fn, a, b, expected)
    setattr(Tests, "test_%s_%s" % (name, lev_fn.__name__), test_fn)


if __name__ == '__main__:
    unittest.main()
