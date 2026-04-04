class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (k + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            new_dp = [0] * (k + 1)
            prefix = 0
            
            for j in range(0, k + 1):
                prefix += dp[j]
                if j >= i:
                    prefix -= dp[j - i]
                
                new_dp[j] = prefix % MOD
            
            dp = new_dp
        
        return dp[k]