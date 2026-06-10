class Solution:
    def minOperations(self, nums):
        ans = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                need = nums[i - 1] + 1
                ans += need - nums[i]
                nums[i] = need

        return ans