class Solution:
    def findMaxLength(self, nums):
        mp = {0: -1}
        pref = 0
        ans = 0
        
        for i, x in enumerate(nums):
            pref += 1 if x == 1 else -1
            
            if pref in mp:
                ans = max(ans, i - mp[pref])
            else:
                mp[pref] = i
        
        return ans