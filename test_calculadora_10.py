#python3 test_calculadora.py -v
import unittest
from calculadora import calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = calculadora()
    
    def test_smoke(self):
        self.assertEquals(2, 2)
    
    def test_sumar_dos_mas_dos(self):
        resultado = self.calc.sumar(2,2)
        self.assertEqual(4, resultado, "El resultado no fue lo esperado")

    def test_sumar_cinco_mas_siete(self):
        resultado = self.calc.sumar(5,7)
        self.assertEqual(12, resultado, "El resultado no fue lo esperado")

if __name__ == '__main__':
    unittest.main(verbosity=2)