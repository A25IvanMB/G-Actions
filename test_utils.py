'''
import unittest
import sys
from utils import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizz_buzz(3), "fizz")
        self.assertEqual(fizz_buzz(6), "fizz")
        self.assertEqual(fizz_buzz(9), "fizz")

    def test_buzz(self):
        self.assertEqual(fizz_buzz(5), "buzz")
        self.assertEqual(fizz_buzz(10), "buzz")
        self.assertEqual(fizz_buzz(20), "buzz")

    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(15), "fizz buzz")
        self.assertEqual(fizz_buzz(30), "fizz buzz")
        self.assertEqual(fizz_buzz(45), "fizz buzz")

    def test_neither(self):
        self.assertEqual(fizz_buzz(1), 1)
        self.assertEqual(fizz_buzz(2), 2)
        self.assertEqual(fizz_buzz(7), 7)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
            print(fizz_buzz(num))
        except ValueError:
            print("Debes ingresar un número entero válido.")
    else:
        unittest.main()

'''
import sys
import unittest
from utils import mayor_de_tres

class TestMayorDeTres(unittest.TestCase):
    def test_primer_numero_es_mayor(self):
        self.assertEqual(mayor_de_tres(5, 3, 2), 5)
        self.assertEqual(mayor_de_tres(10, 0, -1), 10)

    def test_segundo_numero_es_mayor(self):
        self.assertEqual(mayor_de_tres(1, 7, 3), 7)
        self.assertEqual(mayor_de_tres(-1, 5, 0), 5)

    def test_tercer_numero_es_mayor(self):
        self.assertEqual(mayor_de_tres(2, 4, 8), 8)
        self.assertEqual(mayor_de_tres(-5, -3, -1), -1)

    def test_todos_iguales(self):
        self.assertEqual(mayor_de_tres(3, 3, 3), 3)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
            print(f"El mayor de los tres números es: {mayor_de_tres(a, b, c)}")
        except ValueError:
            print("Debes ingresar tres números válidos.")
    else:
        unittest.main()
