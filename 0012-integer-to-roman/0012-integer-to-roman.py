class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of integer values to Roman numerals
        val_to_roman = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        roman = ""
        for val, symbol in val_to_roman:
            # Determine how many times the current symbol fits
            count = num // val
            roman += symbol * count
            num -= val * count
        return roman
