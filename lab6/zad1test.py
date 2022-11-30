import unittest
from zad1 import Operacje

class extest(unittest.TestCase):
    def test_suma_3arg(self):
        op = Operacje()
        self.assertEqual(op.suma(1, 2, 3), 4)

    def test_suma_2arg(self):
        op = Operacje()
        self.assertEqual(op.suma(1, 2), 5)

    def test_suma_1arg(self):
        op = Operacje()
        self.assertEqual(op.suma(1), None)

    def test_suma_0arg(self):
        op = Operacje()
        with self.assertRaises(TypeError):
            op.suma()
    
    def test_roznica_2arg(self):
        op = Operacje()
        self.assertEqual(op.roznica(2, 1), 4)

    def test_roznica_1arg(self):
        op = Operacje()
        self.assertEqual(op.roznica(2), 5)

    def test_roznica_0arg(self):
        op = Operacje()
        self.assertEqual(op.roznica(), 6)

    def test_zmiana_zawartosci(self):
        op=Operacje()
        op['suma']=[1,2]
        op['roznica']=[1,2,3]
        self.assertEqual(op.argumentySuma, [1,2])
        self.assertEqual(op.argumentyRoznica, [1,2,3])

if __name__ == '__main__':
    unittest.main(exit=False)
