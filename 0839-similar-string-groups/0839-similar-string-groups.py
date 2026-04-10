class Solution:
    def numSimilarGroups(self, strs):
        def similar(a, b):
            diff = sum(x != y for x, y in zip(a, b))
            return diff <= 2
        
        parent = list(range(len(strs)))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            parent[find(a)] = find(b)
        
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if similar(strs[i], strs[j]):
                    union(i, j)
        
        return len(set(find(i) for i in range(len(strs))))