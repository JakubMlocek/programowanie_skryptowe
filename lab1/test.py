import main
import unittest

class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
        self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_fraction_fraction(self):
        self.assertEqual(main.sum('1/5','3/10'),0.5)

    def test_sum_complex_complex(self):
        self.assertEqual(main.sum('2+3j','6+j'), (8+4j))
        
    def test_sum_integer_wrong_number_in_string(self):
        self.assertEqual(main.sum(2, 'Ala ma kota123'), 2)
        with self.assertRaises(TypeError):
            raise TypeError
    
    def test_sum_integer_with_list(self):
        self.assertEqual(main.sum(2, [1,3,4]), 2)
        with self.assertRaises(TypeError):
            raise TypeError


if __name__ == '__main__':
    unittest.main()
