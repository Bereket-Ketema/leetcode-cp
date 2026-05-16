class Solution:
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        
        i = 0
        while i < len(nums) and nums[i] < 0 and k > 0:
            nums[i] *= -1
            i += 1
            k -= 1
        
        total = sum(nums)
        
        if k % 2:
            total -= 2 * min(nums)
        
        return total