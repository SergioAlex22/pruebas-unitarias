import unittest
import funcion2

class TestUtils(unittest.TestCase):

    def test_cubic(self):
        self.assertEqual(funcion2.cubic(2), 8)
        self.assertEqual(funcion2.cubic(-2), -8)
        self.assertNotEqual(funcion2.cubic(2), 4)
        self.assertNotEqual(funcion2.cubic(-3), 27)

if __name__ == '__main__':
    unittest.main()