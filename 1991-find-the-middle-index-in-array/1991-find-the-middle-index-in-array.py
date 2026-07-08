class Solution:
    def findMiddleIndex(self, nums):
        total = sum(nums)
        left = 0
        
        for i, x in enumerate(nums):
            if left == total - left - x:
                return i
            left += x
        
        return -1