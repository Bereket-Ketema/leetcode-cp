class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        pointer = -1
        carry = 0
        digits[pointer] += 1 

        while len(digits) >= (-1 * pointer):
            digits[pointer] += carry 
            if digits[pointer] >= 10:
                digits[pointer] = 0
                carry = 1
                pointer -= 1
            else:
                carry = 0
                break

        if carry == 0:
            return digits
        else:
            digits.insert(0, 1)
            return digits 