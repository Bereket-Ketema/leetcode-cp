from functools import lru_cache

class Solution:
    def ways(self, pizza, k):
        m,n = len(pizza), len(pizza[0])
        pre = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                pre[i][j] = (pizza[i][j]=='A') + pre[i+1][j] + pre[i][j+1] - pre[i+1][j+1]
        
        @lru_cache(None)
        def dfs(r,c,cuts):
            if pre[r][c] == 0:
                return 0
            if cuts == 1:
                return 1
            
            res = 0
            MOD = 10**9+7
            
            for nr in range(r+1,m):
                if pre[r][c] > pre[nr][c]:
                    res += dfs(nr,c,cuts-1)
            
            for nc in range(c+1,n):
                if pre[r][c] > pre[r][nc]:
                    res += dfs(r,nc,cuts-1)
            
            return res % MOD
        
        return dfs(0,0,k)