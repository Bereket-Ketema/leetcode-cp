from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums):
        dp = [defaultdict(int) for _ in nums]
        res = 0
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = dp[j][diff]
                res += cnt
                dp[i][diff] += cnt + 1
        
        return res