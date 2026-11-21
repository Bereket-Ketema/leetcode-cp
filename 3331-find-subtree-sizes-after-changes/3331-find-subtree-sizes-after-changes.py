from collections import defaultdict
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = defaultdict(list)
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        ancestors = defaultdict(list)
        
        def dfs_reparent(u: int) -> None:
            char = s[u]
            if ancestors[char]:
                new_parent[u] = ancestors[char][-1]
                
            ancestors[char].append(u)
            for v in adj[u]:
                dfs_reparent(v)
            ancestors[char].pop()
            
        dfs_reparent(0)
        
        new_adj = defaultdict(list)
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [1] * n
        
        def dfs_size(u: int) -> int:
            total = 1
            for v in new_adj[u]:
                total += dfs_size(v)
            ans[u] = total
            return total
            
        dfs_size(0)
        return ans