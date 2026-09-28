import unittest
from x import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add_numbers(2, 3), 5)

if __name__ == "__main__":
    unittest.main()