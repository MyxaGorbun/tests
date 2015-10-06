import unittest
import lib
import math

class LibTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(lib.sin(0), 0)
    def test2(self):
        self.assertEqual(lib.sin(math.pi / 6), 0.5)
    def test3(self):
        self.assertEqual(lib.sin(math.pi / 2), 1)
    def test4(self):
        self.assertEqual(lib.sin(math.pi), 0)
    def test5(self):
        self.assertEqual(lib.sin(3 * math.pi / 2), -1)

unittest.main(verbosity=2)