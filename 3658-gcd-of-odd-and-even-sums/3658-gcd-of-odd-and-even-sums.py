import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd, even= 0, 0
        for i in range(1,2*n+1):
            if i %2 ==0:
                even += i
            else:
                odd +=i
        gcd = math.gcd(odd, even)
        return gcd