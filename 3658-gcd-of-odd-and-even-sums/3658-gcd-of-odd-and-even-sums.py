import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd, even= 0, 0
        for i in range(1,2*n,2):
            odd += i
        for i in range(2,2*n+1,2):
            even += i
        gcd = math.gcd(odd, even)
        return gcd
        