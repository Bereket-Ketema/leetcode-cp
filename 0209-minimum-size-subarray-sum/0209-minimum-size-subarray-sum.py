class Solution:
    def minSubArrayLen(self, target: int, nums):
        left = 0
        store = 0
        min_len = float('inf')

        for right in range(len(nums)):
            store += nums[right]

            while store >= target:
                min_len = min(min_len, right - left + 1)
                store -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len