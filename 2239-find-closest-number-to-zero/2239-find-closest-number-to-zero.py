class Solution:
    def findClosestNumber(self, nums):
        ans = nums[0]

        for x in nums:
            if abs(x) < abs(ans):
                ans = x
            elif abs(x) == abs(ans):
                ans = max(ans, x)

        return ans