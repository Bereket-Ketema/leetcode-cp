class Solution:
    def countPrimeSetBits(self, left, right):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        ans = 0
        
        for num in range(left, right + 1):
            if bin(num).count("1") in primes:
                ans += 1
        
        return ans