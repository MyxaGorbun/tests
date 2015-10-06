import unittest
import lib

class LibTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(lib.palindrome('1'), True)
    def test2(self):
        self.assertEqual(lib.palindrome('11'), True)
    def test3(self):
        self.assertEqual(lib.palindrome('101'), True)
    def test4(self):
        self.assertEqual(lib.palindrome('a'), True)
    def test5(self):
        self.assertEqual(lib.palindrome('aa'), True)
    def test6(self):
        self.assertEqual(lib.palindrome('aha'), True)
    def test7(self):
        self.assertEqual(lib.palindrome('арозаупаланалапуазора'), True)


unittest.main(verbosity=2)