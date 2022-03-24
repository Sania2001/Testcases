import unittest

def check(x):
    if x%7==0:
        return True
    else:
        return False

class Divisible(unittest.TestCase):
    def test_c1(self):
        x=14
        result = check(x)
        self.assertTrue(result)

    def test_c2(self):
        x=15
        result = check(x)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()