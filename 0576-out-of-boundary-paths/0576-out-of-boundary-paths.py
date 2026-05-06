from functools import lru_cache

class Solution:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        MOD = 10**9+7
        
        @lru_cache(None)
        def dfs(r,c,moves):
            if r<0 or c<0 or r>=m or c>=n:
                return 1
            if moves == 0:
                return 0
            
            return (
                dfs(r+1,c,moves-1)+
                dfs(r-1,c,moves-1)+
                dfs(r,c+1,moves-1)+
                dfs(r,c-1,moves-1)
            ) % MOD
        
        return dfs(startRow,startColumn,maxMove)