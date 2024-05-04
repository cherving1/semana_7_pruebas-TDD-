import math
# Definimos la función mcd para calcular el Máximo Común Divisor (MCD) de dos números
def mcd(nro1, nro2):
    # Definimos una función interna para verificar si un número es divisible por otro
    def es_divisible(nro, i):
        # Restamos i de nro hasta que nro sea menor que i
        while nro >= i:
            nro = nro - i
        # Si nro es 0, entonces nro es divisible por i
        return nro == 0

    # Determinamos cuál de los dos números es el menor
    if nro1 > nro2:
        menor = nro2
    else:
        menor = nro1

    # Probamos todos los números desde 1 hasta el número menor
    for i in range(1, menor+1):
        # Si nro1 y nro2 son divisibles por i, entonces i es un divisor común
        if es_divisible(nro1, i) and es_divisible(nro2, i):
            # Guardamos el divisor común más grande encontrado hasta ahora
            mcd = i
            
    # Devolvemos el MCD de nro1 y nro2
    return mcd

# Definimos una función para calcular el MCD de cuatro números
def mcd_cuatro_numeros(a, b, c, d): 
    return mcd(mcd(mcd(a, b), c), d)
import unittest
class TestMCD(unittest.TestCase):
    # Prueba para la función mcd
    def test_mcd(self):
        # Verificamos que la función mcd devuelve el resultado correcto para algunos casos de prueba
        self.assertEqual(mcd(48, 18), 6)
        self.assertEqual(mcd(101, 103), 1)
    # Prueba para la función mcd_cuatro_numeros
    def test_mcd_cuatro_numeros(self):
        # Verificamos que la función mcd_cuatro_numeros devuelve el resultado correcto para algunos casos de prueba
        self.assertEqual(mcd_cuatro_numeros(48, 18, 101, 103), 1)
        self.assertEqual(mcd_cuatro_numeros(48, 24, 36, 60), 12)
if __name__ == '__main__':
    unittest.main()
