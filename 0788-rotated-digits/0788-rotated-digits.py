class Solution:
    def rotatedDigits(self, n):
        good = {'2','5','6','9'}
        bad = {'3','4','7'}
        
        ans = 0
        
        for num in range(1, n+1):
            s = str(num)
            
            if any(c in bad for c in s):
                continue
            
            if any(c in good for c in s):
                ans += 1
        
        return ans