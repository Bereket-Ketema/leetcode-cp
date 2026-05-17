class Solution:
    def maxPower(self, s):
        ans = cur = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                cur = 1
            
            ans = max(ans, cur)
        
        return ans