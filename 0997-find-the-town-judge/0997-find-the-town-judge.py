class Solution:
    def findJudge(self, n, trust):
        indeg = [0]*(n+1)
        outdeg = [0]*(n+1)
        
        for a,b in trust:
            outdeg[a] += 1
            indeg[b] += 1
        
        for i in range(1,n+1):
            if indeg[i] == n-1 and outdeg[i] == 0:
                return i
        
        return -1