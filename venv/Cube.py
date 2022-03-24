import unittest


def Cube(x):
    return x*x*x

class volume(unittest.TestCase):
    def test_volume(self):
        a = 5.555
        result = Cube(a)
        self.assertAlmostEqual(a*a*a,result)


if __name__ == "__main__":
    unittest.main()