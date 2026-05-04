from collections import defaultdict

class Solution:
    def criticalConnections(self, n, connections):
        g=defaultdict(list)
        for u,v in connections:
            g[u].append(v)
            g[v].append(u)
        
        disc=[-1]*n
        low=[0]*n
        time=0
        res=[]
        
        def dfs(u,parent):
            nonlocal time
            disc[u]=low[u]=time
            time+=1
            
            for v in g[u]:
                if v==parent:
                    continue
                if disc[v]==-1:
                    dfs(v,u)
                    low[u]=min(low[u],low[v])
                    if low[v]>disc[u]:
                        res.append([u,v])
                else:
                    low[u]=min(low[u],disc[v])
        
        dfs(0,-1)
        return res