import unittest
from Bookean38 import Boolean38

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Boolean38(3, 1, 6, 6), False)
        self.assertEqual(Boolean38(4, 4, 2, 6), True)


if __name__ == '__main__':
    unittest.main()
