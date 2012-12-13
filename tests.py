import unittest
import pylev


class ClassicLevenschteinTestCase(unittest.TestCase):
    def test_classic(self):
        self.assertEqual(pylev.classic_levenschtein('kitten', 'sitting'), 3)

    def test_same(self):
        self.assertEqual(pylev.classic_levenschtein('kitten', 'kitten'), 0)

    def test_empty(self):
        self.assertEqual(pylev.classic_levenschtein('', ''), 0)

    def test_long(self):
        self.assertEqual(pylev.classic_levenschtein('confide', 'deceit'), 6)

    def test_painful(self):
        # This is pretty slow but should work.
        self.assertEqual(pylev.classic_levenschtein('CUNsperrICY', 'conspiracy'), 8)


class LevenschteinTestCase(unittest.TestCase):
    def test_classic(self):
        self.assertEqual(pylev.levenschtein('kitten', 'sitting'), 3)

    def test_same(self):
        self.assertEqual(pylev.levenschtein('kitten', 'kitten'), 0)

    def test_empty(self):
        self.assertEqual(pylev.levenschtein('', ''), 0)

    def test_long(self):
        self.assertEqual(pylev.levenschtein('confide', 'deceit'), 6)

    def test_painful(self):
        # This is much faster than the above.
        self.assertEqual(pylev.levenschtein('CUNsperrICY', 'conspiracy'), 8)
