import unittest
from Array100 import Array100

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Array100([2, 3, 1, 7, 1]), [2, 3, 7])
        self.assertEqual(Array100([2, 3, 1, 7]), [2, 3, 7, 1])


if __name__ == '__main__':
    unittest.main()
