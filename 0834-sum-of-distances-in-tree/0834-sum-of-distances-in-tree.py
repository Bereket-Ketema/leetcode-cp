class Solution:
    def sumOfDistancesInTree(self, n, edges):
        from collections import defaultdict
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        count = [1]*n
        res = [0]*n
        
        def dfs(node, parent):
            for nei in g[node]:
                if nei == parent: continue
                dfs(nei, node)
                count[node] += count[nei]
                res[node] += res[nei] + count[nei]
        
        def dfs2(node, parent):
            for nei in g[node]:
                if nei == parent: continue
                res[nei] = res[node] - count[nei] + (n - count[nei])
                dfs2(nei, node)
        
        dfs(0,-1)
        dfs2(0,-1)
        return res