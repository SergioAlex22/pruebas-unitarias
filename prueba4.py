import unittest
import funcion2

class TestUtils(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(funcion2.say_hello("Geekflare"), "Hola, Geekflare")
        self.assertEqual(funcion2.say_hello("Chandan"), "Hola, Chandan")
        self.assertNotEqual(funcion2.say_hello("Chandan"), "Hi, Chandan")
        self.assertNotEqual(funcion2.say_hello("Hafeez"), "Hi, Hafeez")

if __name__ == '__main__':
    unittest.main()