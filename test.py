import unittest
from main import RomanstoInt

class RomanstoIntTest(unittest.TestCase):

    def setUp(self):
        self.converter = RomanstoInt()

    def test_roman_to_int(self):
        self.assertEqual(self.converter.roman_to_int('III'), 3)
        self.assertEqual(self.converter.roman_to_int('IV'), 4)
        self.assertEqual(self.converter.roman_to_int('IX'), 9)
        self.assertEqual(self.converter.roman_to_int('LVIII'), 58)
        self.assertEqual(self.converter.roman_to_int('MCMXCIV'), 1994)

    def test_int_to_roman(self):
        self.assertEqual(self.converter.int_to_roman(3), 'III')
        self.assertEqual(self.converter.int_to_roman(4), 'IV')
        self.assertEqual(self.converter.int_to_roman(9), 'IX')
        self.assertEqual(self.converter.int_to_roman(58), 'LVIII')
        self.assertEqual(self.converter.int_to_roman(1994), 'MCMXCIV')

    def test_combine_roman_numerals(self):
        self.assertEqual(self.converter.combine_roman_numerals('III', 'IV'), 7)
        self.assertEqual(self.converter.combine_roman_numerals('IV', 'IX'), 13)
        self.assertEqual(self.converter.combine_roman_numerals('LVIII', 'MCMXCIV'), 2052)
        self.assertEqual(self.converter.combine_roman_numerals('CD', 'XL'), 440)

if __name__ == '__main__':
    unittest.main()
