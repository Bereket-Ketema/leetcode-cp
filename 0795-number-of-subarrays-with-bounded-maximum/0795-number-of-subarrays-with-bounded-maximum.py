class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):
        def count(bound):
            cur = res = 0
            for num in nums:
                if num <= bound:
                    cur += 1
                else:
                    cur = 0
                res += cur
            return res
        
        return count(right) - count(left - 1)