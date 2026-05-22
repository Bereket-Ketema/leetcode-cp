class Solution:
    def minTrioDegree(self, n, edges):
        g = [[False]*(n+1) for _ in range(n+1)]
        deg = [0]*(n+1)
        
        for u,v in edges:
            g[u][v] = g[v][u] = True
            deg[u] += 1
            deg[v] += 1
        
        ans = float('inf')
        
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if g[i][j]:
                    for k in range(j+1,n+1):
                        if g[i][k] and g[j][k]:
                            ans = min(ans,
                                      deg[i]+deg[j]+deg[k]-6)
        
        return ans if ans != float('inf') else -1