class Solution:
    def prefixesDivBy5(self, nums):
        cur = 0
        ans = []
        
        for x in nums:
            cur = (cur * 2 + x) % 5
            ans.append(cur == 0)
        
        return ans