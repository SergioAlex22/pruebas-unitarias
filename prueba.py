import unittest

from funcion1 import *

class TestOperaciones(unittest.TestCase):
    def setUp(self):
        pass

    def test_suma(self):
        espera=3
        actual=suma(1,2)
        self.assertEqual(actual,espera)
    
    def test_resta(self):
        espera=5
        actual=resta(10,5)
        self.assertEqual(actual,espera)
    
    def test_multi(self):
        espera=50
        actual=multi(10,5)
        self.assertEqual(actual,espera)

    def test_div(self):
        espera=6
        actual=div(12,2)
        self.assertEqual(actual,espera)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
        