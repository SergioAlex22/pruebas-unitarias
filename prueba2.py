import unittest

import funcion2


class TestUtils(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(funcion2.is_prime(4))
        self.assertTrue(funcion2.is_prime(2))
        self.assertTrue(funcion2.is_prime(3))
        self.assertFalse(funcion2.is_prime(8))
        self.assertFalse(funcion2.is_prime(10))
        self.assertTrue(funcion2.is_prime(7))
        self.assertEqual(funcion2.is_prime(-3),
                         "No se admiten numeros negativos")


if __name__ == '__main__':
    unittest.main()