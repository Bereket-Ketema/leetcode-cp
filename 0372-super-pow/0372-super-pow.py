class Solution:
    def superPow(self, a, b):
        mod = 1337
        
        def powmod(x, n):
            res = 1
            x %= mod
            for _ in range(n):
                res = (res * x) % mod
            return res
        
        res = 1
        for digit in b:
            res = powmod(res, 10) * powmod(a, digit) % mod
        
        return res