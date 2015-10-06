import unittest
import lib

class LibTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(lib.factorial(1), 1)
    def test2(self):
        self.assertEqual(lib.factorial(-1), 1)
    def test3(self):
        self.assertEqual(lib.factorial(3), 6)
    def test4(self):
        self.assertEqual(lib.factorial(0), 1)
unittest.main(verbosity=2)