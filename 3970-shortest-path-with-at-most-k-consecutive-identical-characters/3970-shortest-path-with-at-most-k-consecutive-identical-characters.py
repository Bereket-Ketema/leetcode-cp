import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if n == 1:
            return 0 if k >= 1 else -1

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        dist = {}
        pq = [(0, 0, 1)]
        dist[(0, 1)] = 0

        while pq:
            d, u, run_len = heapq.heappop(pq)

            if d > dist.get((u, run_len), float('inf')):
                continue

            if u == n - 1:
                return d

            curr_char = labels[u]

            for v, w in adj[u]:
                next_char = labels[v]
                next_run_len = run_len + 1 if next_char == curr_char else 1

                if next_run_len <= k:
                    new_dist = d + w
                    if new_dist < dist.get((v, next_run_len), float('inf')):
                        dist[(v, next_run_len)] = new_dist
                        heapq.heappush(pq, (new_dist, v, next_run_len))

        return -1