from collections import Counter

class Solution:
    def findPairs(self, nums, k):
        c = Counter(nums)
        ans = 0
        
        if k == 0:
            for v in c.values():
                if v > 1:
                    ans += 1
        else:
            for x in c:
                if x + k in c:
                    ans += 1
        
        return ans