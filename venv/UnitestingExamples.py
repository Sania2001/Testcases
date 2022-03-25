
# def add(a,b):
#     return a+b;
#
# result = add(2,3)
# print (result)
import sys
import unittest

def add(x, y):

    return x+y


class MyApp1(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith("darwin"),"require windows os")
    def test_case1(self):
        a = 10
        b = 22
        c = add(a, b)
        self.assertEqual(32,c)

    @unittest.skip("skipped")
    def test_case2(self):
        a = 5.2
        b = 3.1
        result = add(a,b)
        self.assertEqual(a+b,result)


if __name__ == "__main__":
    unittest.main()