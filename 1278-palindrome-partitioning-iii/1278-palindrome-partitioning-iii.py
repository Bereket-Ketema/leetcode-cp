from functools import lru_cache

class Solution:
    def palindromePartition(self, s, k):
        n = len(s)
        
        cost = [[0]*n for _ in range(n)]
        
        for length in range(2,n+1):
            for i in range(n-length+1):
                j = i+length-1
                
                cost[i][j] = cost[i+1][j-1] + (s[i] != s[j])
        
        @lru_cache(None)
        def dfs(i,k):
            if k == 1:
                return cost[i][n-1]
            
            ans = float('inf')
            
            for j in range(i,n-k+1):
                ans = min(ans,
                          cost[i][j] + dfs(j+1,k-1))
            
            return ans
        
        return dfs(0,k)