class Solution:
    def nthSuperUglyNumber(self, n, primes):
        k = len(primes)
        idx = [0] * k
        ugly = [1]
        
        for _ in range(1, n):
            next_val = min(primes[i] * ugly[idx[i]] for i in range(k))
            ugly.append(next_val)
            
            for i in range(k):
                if primes[i] * ugly[idx[i]] == next_val:
                    idx[i] += 1
        
        return ugly[-1]