from functools import lru_cache

class Solution:
    def largestSumOfAverages(self, nums, k):
        n = len(nums)
        
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        def avg(i, j):
            return (prefix[j] - prefix[i]) / (j - i)
        
        @lru_cache(None)
        def dp(i, groups):
            if groups == 1:
                return avg(i, n)
            
            best = 0
            
            for j in range(i+1, n-groups+2):
                best = max(
                    best,
                    avg(i, j) + dp(j, groups-1)
                )
            
            return best
        
        return dp(0, k)