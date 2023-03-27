class RomanstoInt:
    roman_numerals = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
                      'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    def roman_to_int(self, s: str) -> int:
        """
        Converts a Roman numeral to an integer.
        """
        result = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in self.roman_numerals:
                result += self.roman_numerals[s[i:i + 2]]
                i += 2
            else:
                result += self.roman_numerals[s[i]]
                i += 1
        return result

    def int_to_roman(self, num: int) -> str:
        """
        Converts an integer to a Roman numeral.
        """
        result = ''
        for numeral, value in self.roman_numerals.items():
            while num >= value:
                result += numeral
                num -= value
        return result

    def combine_roman_numerals(self, s1: str, s2: str) -> int:
        """
        Combines two Roman numerals to make a new one.
        """
        num1 = self.roman_to_int(s1)
        num2 = self.roman_to_int(s2)
        return num1 + num2

converter = RomanstoInt()

# Create an instance of the RomanNumeralConverter class
converter = RomanstoInt()

# Convert a Roman numeral to an integer
print(converter.roman_to_int('XXI'))  # Output: 21

# Convert an integer to a Roman numeral
print(converter.int_to_roman(27))  # Output: 'MMXXIII'

# Combine two Roman numerals to make a new one
print(converter.combine_roman_numerals('X', 'VIII'))  # Output: 'XVIII'

