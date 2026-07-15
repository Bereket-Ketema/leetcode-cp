class Solution:
    def maximumDifference(self, nums):
        mn = nums[0]
        ans = -1

        for x in nums[1:]:
            if x > mn:
                ans = max(ans, x - mn)
            mn = min(mn, x)

        return ans