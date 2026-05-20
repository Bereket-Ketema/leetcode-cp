class Solution:
    def maxNiceDivisors(self, primeFactors):
        MOD = 10**9+7
        
        if primeFactors <= 3:
            return primeFactors
        
        if primeFactors % 3 == 0:
            return pow(3, primeFactors//3, MOD)
        
        if primeFactors % 3 == 1:
            return pow(3, (primeFactors-4)//3, MOD) * 4 % MOD
        
        return pow(3, primeFactors//3, MOD) * 2 % MOD