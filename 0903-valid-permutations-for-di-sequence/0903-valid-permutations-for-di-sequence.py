class Solution:
    def numPermsDISequence(self, s):
        MOD = 10**9+7
        n = len(s)

        dp = [1]*(n+1)

        for i,c in enumerate(s):
            ndp = [0]*(n+1)

            if c == 'I':
                cur = 0
                for j in range(n-i):
                    cur = (cur + dp[j]) % MOD
                    ndp[j] = cur
            else:
                cur = 0
                for j in range(n-i-1,-1,-1):
                    cur = (cur + dp[j+1]) % MOD
                    ndp[j] = cur

            dp = ndp

        return dp[0]