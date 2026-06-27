from collections import deque

class Solution:
    def getAncestors(self, n, edges):
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        ancestors = [set() for _ in range(n)]
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()

            for v in graph[u]:
                ancestors[v].add(u)
                ancestors[v].update(ancestors[u])

                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return [sorted(list(s)) for s in ancestors]