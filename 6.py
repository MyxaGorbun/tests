import unittest
import lib

class LibTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(lib.sqrt(0), 0)
    def test2(self):
        self.assertEqual(lib.sqrt(1), 1)
    def test3(self):
        self.assertEqual(lib.sqrt(-1), 0)

unittest.main(verbosity=2)