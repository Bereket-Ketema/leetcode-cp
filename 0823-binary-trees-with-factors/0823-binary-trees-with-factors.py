class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        
        arr.sort()
        dp = {}
        
        for x in arr:
            dp[x] = 1
        
        s = set(arr)
        
        for x in arr:
            for y in arr:
                if y * y > x:
                    break
                
                if x % y == 0:
                    z = x // y
                    
                    if z in s:
                        if y == z:
                            dp[x] += dp[y] * dp[z]
                        else:
                            dp[x] += dp[y] * dp[z] * 2
                        
                        dp[x] %= MOD
        
        return sum(dp.values()) % MOD