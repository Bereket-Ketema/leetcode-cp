class Solution:
    def largestAltitude(self, gain):
        cur = 0
        ans = 0
        
        for x in gain:
            cur += x
            ans = max(ans, cur)
        
        return ans