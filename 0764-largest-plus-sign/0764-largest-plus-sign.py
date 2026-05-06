class Solution:
    def orderOfLargestPlusSign(self, n, mines):
        banned = set(map(tuple,mines))
        dp = [[n]*n for _ in range(n)]
        
        for i in range(n):
            cnt = 0
            for j in range(n):
                cnt = 0 if (i,j) in banned else cnt+1
                dp[i][j] = min(dp[i][j],cnt)
            
            cnt = 0
            for j in range(n-1,-1,-1):
                cnt = 0 if (i,j) in banned else cnt+1
                dp[i][j] = min(dp[i][j],cnt)
        
        for j in range(n):
            cnt = 0
            for i in range(n):
                cnt = 0 if (i,j) in banned else cnt+1
                dp[i][j] = min(dp[i][j],cnt)
            
            cnt = 0
            for i in range(n-1,-1,-1):
                cnt = 0 if (i,j) in banned else cnt+1
                dp[i][j] = min(dp[i][j],cnt)
        
        return max(max(row) for row in dp)