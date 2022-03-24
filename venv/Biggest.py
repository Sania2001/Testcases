import unittest


def check(x,y):
    if x>y:
        return x
    else:
        return y


class biggest(unittest.TestCase):

    def test_biggest(self):
        a=10
        b=5
        z= check(a,b)
        p= max(a,b)
        self.assertEqual(p,z)

if __name__ == "__main__":
    unittest.main()

