class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l, r = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while l >= 0 or r >= 0 or carry:
            d1 = ord(num1[l]) - 48 if l >= 0 else 0
            d2 = ord(num2[r]) - 48 if r >= 0 else 0

            total = d1 + d2 + carry
            result.append(str(total % 10))
            carry = total // 10

            l -= 1
            r -= 1

        return ''.join(reversed(result))
