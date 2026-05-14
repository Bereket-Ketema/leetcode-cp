class Solution:
    def findRedundantDirectedConnection(self, edges):
        parent = {}
        cand1 = cand2 = None
        
        for u,v in edges:
            if v in parent:
                cand1 = [parent[v], v]
                cand2 = [u, v]
            else:
                parent[v] = u
        
        def find(x):
            while uf[x] != x:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x
        
        def union(x,y):
            px, py = find(x), find(y)
            if px == py:
                return False
            uf[py] = px
            return True
        
        uf = list(range(len(edges)+1))
        
        for u,v in edges:
            if [u,v] == cand2:
                continue
            if not union(u,v):
                return cand1 if cand1 else [u,v]
        
        return cand2