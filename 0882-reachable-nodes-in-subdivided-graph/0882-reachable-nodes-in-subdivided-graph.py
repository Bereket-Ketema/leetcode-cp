import heapq
from collections import defaultdict

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        g = defaultdict(list)

        for u,v,w in edges:
            g[u].append((v,w))
            g[v].append((u,w))

        pq = [(-maxMoves,0)]
        dist = {}

        while pq:
            moves,node = heapq.heappop(pq)
            moves = -moves

            if node in dist:
                continue
            dist[node] = moves

            for nei,w in g[node]:
                nm = moves-w-1
                if nm >= 0 and nei not in dist:
                    heapq.heappush(pq,(-nm,nei))

        ans = len(dist)

        for u,v,w in edges:
            a = dist.get(u,0)
            b = dist.get(v,0)
            ans += min(w,a+b)

        return ans