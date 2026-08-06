class Solution:
    def getMinDistance(self, nums, target, start):
        ans = float("inf")

        for i, x in enumerate(nums):
            if x == target:
                ans = min(ans, abs(i - start))

        return ans