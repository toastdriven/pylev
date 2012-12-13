import unittest2
import pylev


class LevenschteinTestCase(unittest2.TestCase):
    def test_classic(self):
        self.assertEqual()
        self.assertEqual(pylev.levenschtein('kitten', 'sitting'), 3)

    def test_same(self):
        self.assertEqual(pylev.levenschtein('kitten', 'kitten'), 0)

    def test_empty(self):
        self.assertEqual(pylev.levenschtein('', ''), 0)

    def test_long(self):
        self.assertEqual(pylev.levenschtein('confide', 'deceit'), 6)
