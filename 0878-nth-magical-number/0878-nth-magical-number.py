class Solution:
    def nthMagicalNumber(self, n, a, b):
        MOD = 10**9 + 7
        
        def gcd(x,y):
            while y:
                x,y = y,x%y
            return x
        
        lcm = a*b // gcd(a,b)
        
        l,r = 1, n*min(a,b)
        
        while l < r:
            m = (l+r)//2
            
            cnt = m//a + m//b - m//lcm
            
            if cnt < n:
                l = m+1
            else:
                r = m
        
        return l % MOD