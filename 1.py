import unittest
import lib

class LibTest(unittest.TestCase):
    def test1(self):
        self.assertFalse(lib.even(1))
    def test2(self):
        self.assertFalse(lib.even(3))
    def test3(self):
        self.assertFalse(lib.even(5))
    def test4(self):
        self.assertFalse(lib.even(-1))
    def test5(self):
        self.assertFalse(lib.even(0.5))
    def test6(self):
        self.assertTrue(lib.even(0))
    def test7(self):
        self.assertTrue(lib.even(2))
    def test8(self):
        self.assertTrue(lib.even(4))
    def test9(self):
        self.assertTrue(lib.even(6))

unittest.main(verbosity=2)