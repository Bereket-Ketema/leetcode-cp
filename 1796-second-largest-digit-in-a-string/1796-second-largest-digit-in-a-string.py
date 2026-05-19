class Solution:
    def secondHighest(self, s):
        nums = sorted(set(int(c) for c in s if c.isdigit()))
        
        if len(nums) < 2:
            return -1
        
        return nums[-2]