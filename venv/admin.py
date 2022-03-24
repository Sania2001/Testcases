import unittest

def login(username,password):
    if username=='admin' and password=='12345':
        return True
    else:
        return False

class verification(unittest.TestCase):
    def test_login(self):
        result = login("admin","12345")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()