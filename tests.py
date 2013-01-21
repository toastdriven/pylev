import unittest
import pylev


class ClassicLevenshteinTestCase(unittest.TestCase):
    def test_classic(self):
        self.assertEqual(pylev.classic_levenshtein('kitten', 'sitting'), 3)

    def test_same(self):
        self.assertEqual(pylev.classic_levenshtein('kitten', 'kitten'), 0)

    def test_empty(self):
        self.assertEqual(pylev.classic_levenshtein('', ''), 0)

    def test_long(self):
        self.assertEqual(pylev.classic_levenshtein('confide', 'deceit'), 6)

    def test_painful(self):
        # This is pretty slow but should work.
        self.assertEqual(pylev.classic_levenshtein('CUNsperrICY', 'conspiracy'), 8)


class LevenshteinTestCase(unittest.TestCase):
    def test_classic(self):
        self.assertEqual(pylev.levenshtein('kitten', 'sitting'), 3)

    def test_same(self):
        self.assertEqual(pylev.levenshtein('kitten', 'kitten'), 0)

    def test_empty(self):
        self.assertEqual(pylev.levenshtein('', ''), 0)

    def test_long(self):
        self.assertEqual(pylev.levenshtein('confide', 'deceit'), 6)

    def test_painful(self):
        # This is much faster than the above.
        self.assertEqual(pylev.levenshtein('CUNsperrICY', 'conspiracy'), 8)
