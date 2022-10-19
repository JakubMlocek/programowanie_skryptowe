from zad2 import splitter_for_test
import unittest

class TestInputScipt(unittest.TestCase):

    def test_only_text(self):
        self.assertEqual(splitter_for_test('ala'), 'Wyraz:ala')
    
    def test_only_nums(self):
        self.assertEqual(splitter_for_test('123'), 'Liczba:123')

    def test_both(self):
        self.assertEqual(splitter_for_test('ala321'), 'Wyraz:alaLiczba:321')

if __name__ == '__main__':
    unittest.main()