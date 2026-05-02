from functools import lru_cache

class Solution:
    def minDistance(self, houses, k):
        houses.sort()
        n=len(houses)
        
        cost=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                m=(i+j)//2
                for t in range(i,j+1):
                    cost[i][j]+=abs(houses[t]-houses[m])
        
        @lru_cache(None)
        def dp(i,k):
            if k==1:
                return cost[i][n-1]
            res=float('inf')
            for j in range(i,n-k+1):
                res=min(res,cost[i][j]+dp(j+1,k-1))
            return res
        
        return dp(0,k)