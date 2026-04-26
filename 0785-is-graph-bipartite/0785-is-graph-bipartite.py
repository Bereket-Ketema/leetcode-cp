class Solution:
    def isBipartite(self, graph):
        color = {}
        
        for i in range(len(graph)):
            if i not in color:
                stack = [i]
                color[i] = 0
                
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            color[nei] = color[node] ^ 1
                            stack.append(nei)
                        elif color[nei] == color[node]:
                            return False
        return True