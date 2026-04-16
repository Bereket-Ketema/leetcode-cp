class Solution:
    def maxProduct(self, nums):
        cur_max = cur_min = res = nums[0]
        
        for n in nums[1:]:
            temp = cur_max
            cur_max = max(n, n * cur_max, n * cur_min)
            cur_min = min(n, n * temp, n * cur_min)
            res = max(res, cur_max)
        
        return res