class Solution:
    def arrayRankTransform(self, arr):
        rank = {}
        
        for i, num in enumerate(sorted(set(arr)), 1):
            rank[num] = i
        
        return [rank[x] for x in arr]