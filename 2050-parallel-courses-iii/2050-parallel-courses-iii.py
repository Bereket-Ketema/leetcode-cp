from collections import deque

class Solution:
    def minimumTime(self, n, relations, time):
        graph = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)

        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1

        dp = [0] * (n + 1)
        q = deque()

        for i in range(1, n + 1):
            if indegree[i] == 0:
                dp[i] = time[i - 1]
                q.append(i)

        while q:
            u = q.popleft()

            for v in graph[u]:
                dp[v] = max(dp[v], dp[u] + time[v - 1])
                indegree[v] -= 1

                if indegree[v] == 0:
                    q.append(v)

        return max(dp)