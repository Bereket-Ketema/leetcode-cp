class Solution:
    def champagneTower(self, poured, row, glass):
        dp = [poured]
        
        for r in range(1, row + 1):
            new = [0]*(r+1)
            for i in range(len(dp)):
                overflow = max(0, dp[i] - 1) / 2
                new[i] += overflow
                new[i+1] += overflow
            dp = new
        
        return min(1, dp[glass])