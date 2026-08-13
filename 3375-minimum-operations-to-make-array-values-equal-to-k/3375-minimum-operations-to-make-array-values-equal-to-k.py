class Solution:
    def minOperations(self, nums, k):
        values = set(nums)

        if any(x < k for x in nums):
            return -1

        return len(values - {k})