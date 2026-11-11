from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 1)
        
        for j in range(1, n + 1):
            c = costs[j - 1]
            best = dp[j - 1] + 1
            if j >= 2:
                best = min(best, dp[j - 2] + 4)
            if j >= 3:
                best = min(best, dp[j - 3] + 9)
            dp[j] = c + best
            
        return dp[n]