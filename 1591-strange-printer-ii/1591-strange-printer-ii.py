class Solution:
    def isPrintable(self, targetGrid):
        m,n = len(targetGrid), len(targetGrid[0])
        
        colors = {}
        
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                
                if c not in colors:
                    colors[c] = [i,j,i,j]
                else:
                    colors[c][0] = min(colors[c][0],i)
                    colors[c][1] = min(colors[c][1],j)
                    colors[c][2] = max(colors[c][2],i)
                    colors[c][3] = max(colors[c][3],j)
        
        graph = {c:set() for c in colors}
        
        for c,(r1,c1,r2,c2) in colors.items():
            for i in range(r1,r2+1):
                for j in range(c1,c2+1):
                    if targetGrid[i][j] != c:
                        graph[c].add(targetGrid[i][j])
        
        vis = {}
        
        def dfs(u):
            if u in vis:
                return vis[u]
            
            vis[u] = False
            
            for v in graph[u]:
                if dfs(v) == False:
                    return False
            
            vis[u] = True
            return True
        
        return all(dfs(c) for c in colors)