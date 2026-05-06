import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        g = defaultdict(list)
        
        for u,v,w in times:
            g[u].append((v,w))
        
        pq = [(0,k)]
        dist = {}
        
        while pq:
            d,node = heapq.heappop(pq)
            
            if node in dist:
                continue
            
            dist[node] = d
            
            for nei,w in g[node]:
                if nei not in dist:
                    heapq.heappush(pq,(d+w,nei))
        
        return max(dist.values()) if len(dist)==n else -1