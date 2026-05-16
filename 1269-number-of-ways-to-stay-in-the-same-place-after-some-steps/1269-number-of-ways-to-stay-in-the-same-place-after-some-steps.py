class Solution:
    def numWays(self, steps, arrLen):
        MOD = 10**9+7
        maxPos = min(arrLen-1, steps)
        
        dp = [0]*(maxPos+1)
        dp[0] = 1
        
        for _ in range(steps):
            ndp = [0]*(maxPos+1)
            
            for i in range(maxPos+1):
                ndp[i] = dp[i]
                if i > 0:
                    ndp[i] = (ndp[i] + dp[i-1]) % MOD
                if i < maxPos:
                    ndp[i] = (ndp[i] + dp[i+1]) % MOD
            
            dp = ndp
        
        return dp[0]