class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)

        for key in graph:
            graph[key].sort(reverse=True)

        result = []

        def dfs(node):
            while graph[node]:
                next_dest = graph[node].pop()
                dfs(next_dest)
            result.append(node)

        dfs("JFK")
        return result[::-1]