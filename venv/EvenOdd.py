

import unittest

def check(a):
    if a%2==0:
       return "even"
    else:
        return "odd"


class c2(unittest.TestCase):

    def testc2(self):
        x= 12
        y=check(x)

        self.assertEqual("even", y)

    def testc3(self):
        x = 13
        y = check(x)

        self.assertEqual("odd", y)



if __name__ == "__main__":
    unittest.main()