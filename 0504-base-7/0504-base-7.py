class Solution:
    def convertToBase7(self, num: int) -> str:
        result = ''
        a = num
        while num != 0:
            result += str(abs(num) % 7)
            num = abs(num) // 7
        if not result:
            result = '0'
        return result[::-1] if a >= 0 else "-"+result[::-1]