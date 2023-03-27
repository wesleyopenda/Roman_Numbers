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

    def is_valid_roman_numeral(self, s: str) -> bool:
        """
        Check whether a string is a valid Roman numeral.
        """
        for letter in s:
            if letter not in self.roman_numerals:
                return False
        return True

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

# Combine two Roman numerals to make a new one
print(converter.combine_roman_numerals('X', 'VIII'))  # Output: '18'
print(converter.combine_roman_numerals('XX', 'IV'))  # Output: '24'

