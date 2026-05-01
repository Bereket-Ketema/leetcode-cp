class Solution:
    def profitableSchemes(self, n, minProfit, group, profit):
        MOD = 10**9+7
        dp = [[0]*(minProfit+1) for _ in range(n+1)]
        dp[0][0] = 1
        
        for g,p in zip(group, profit):
            for i in range(n, g-1, -1):
                for j in range(minProfit, -1, -1):
                    dp[i][j] += dp[i-g][max(0,j-p)]
                    dp[i][j] %= MOD
        
        return sum(dp[i][minProfit] for i in range(n+1)) % MOD