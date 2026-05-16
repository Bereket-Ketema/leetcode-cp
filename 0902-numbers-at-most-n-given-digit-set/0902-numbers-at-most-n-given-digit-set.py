class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        s = str(n)
        m = len(s)
        d = len(digits)
        
        ans = sum(d**i for i in range(1, m))
        
        for i, ch in enumerate(s):
            smaller = sum(x < ch for x in digits)
            ans += smaller * (d ** (m-i-1))
            
            if ch not in digits:
                return ans
        
        return ans + 1