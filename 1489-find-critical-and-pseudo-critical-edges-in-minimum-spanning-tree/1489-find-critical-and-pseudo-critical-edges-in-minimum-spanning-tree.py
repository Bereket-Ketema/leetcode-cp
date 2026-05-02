class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        edges = [edge + [i] for i, edge in enumerate(edges)]
        edges.sort(key=lambda x: x[2])
        
        class UF:
            def __init__(self, n):
                self.parent = list(range(n))
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, a, b):
                pa, pb = self.find(a), self.find(b)
                if pa == pb:
                    return False
                self.parent[pa] = pb
                return True
        
        def kruskal(skip=-1, force=-1):
            uf = UF(n)
            weight = 0
            edges_used = 0
            
            if force != -1:
                u, v, w, idx = edges[force]
                if uf.union(u, v):
                    weight += w
                    edges_used += 1
            
            for i, (u, v, w, idx) in enumerate(edges):
                if i == skip:
                    continue
                
                if uf.union(u, v):
                    weight += w
                    edges_used += 1
            
            if edges_used == n-1:
                return weight
            return float('inf')
        
        base = kruskal()
        
        critical = []
        pseudo = []
        
        for i in range(len(edges)):
            if kruskal(skip=i) > base:
                critical.append(edges[i][3])
            elif kruskal(force=i) == base:
                pseudo.append(edges[i][3])
        
        return [critical, pseudo]