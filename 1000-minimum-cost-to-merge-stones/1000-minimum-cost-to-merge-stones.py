from functools import lru_cache

class Solution:
    def mergeStones(self, stones, k):
        n = len(stones)
        if (n-1)%(k-1):
            return -1
        
        pre=[0]
        for x in stones:
            pre.append(pre[-1]+x)
        
        @lru_cache(None)
        def dp(i,j):
            if i==j:
                return 0
            
            res=float('inf')
            for m in range(i,j,k-1):
                res=min(res,dp(i,m)+dp(m+1,j))
            
            if (j-i)%(k-1)==0:
                res += pre[j+1]-pre[i]
            
            return res
        
        return dp(0,n-1)