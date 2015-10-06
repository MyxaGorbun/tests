import unittest
import lib

class LibTest(unittest.TestCase):
    def test1(self):
        self.assertFalse(lib.prime(0))
    def test2(self):
        self.assertFalse(lib.prime(6))
    def test3(self):
        self.assertTrue(lib.prime(1))

unittest.main(verbosity=2)