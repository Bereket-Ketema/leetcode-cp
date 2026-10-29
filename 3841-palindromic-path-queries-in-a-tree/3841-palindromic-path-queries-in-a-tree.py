from typing import List
import sys

# Increase recursion depth for deep tree traversals
sys.setrecursionlimit(200000)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOGN = 17
        up = [[0] * LOGN for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative Euler tour / DFS to prevent stack overflow
        order = []
        stack = [(0, -1, 0)]
        visited_idx = [0] * n
        
        while stack:
            u, p, d = stack[-1]
            if visited_idx[u] == 0:
                timer += 1
                tin[u] = timer
                depth[u] = d
                up[u][0] = p if p != -1 else 0
                for k in range(1, LOGN):
                    up[u][k] = up[up[u][k - 1]][k - 1]
            
            if visited_idx[u] < len(adj[u]):
                v = adj[u][visited_idx[u]]
                visited_idx[u] += 1
                if v != p:
                    stack.append((v, u, d + 1))
            else:
                tout[u] = timer
                stack.pop()

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOGN):
                if (diff >> k) & 1:
                    u = up[u][k]
            if u == v:
                return u
            for k in range(LOGN - 1, -1, -1):
                if up[u][k] != up[v][k]:
                    u = up[u][k]
                    v = up[v][k]
            return up[u][0]

        bit = [0] * (n + 2)

        def update(idx: int, val: int):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)

        def query(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        curr_chars = list(s)
        for i in range(n):
            mask = 1 << (ord(curr_chars[i]) - ord('a'))
            update(tin[i], mask)
            update(tout[i] + 1, mask)

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                old_mask = 1 << (ord(curr_chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))
                diff = old_mask ^ new_mask
                if diff != 0:
                    curr_chars[u] = c
                    update(tin[u], diff)
                    update(tout[u] + 1, diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)
                mask_u = query(tin[u])
                mask_v = query(tin[v])
                mask_w = query(tin[w])
                val_w = 1 << (ord(curr_chars[w]) - ord('a'))
                path_mask = mask_u ^ mask_v ^ val_w
                ans.append((path_mask & (path_mask - 1)) == 0)

        return ans