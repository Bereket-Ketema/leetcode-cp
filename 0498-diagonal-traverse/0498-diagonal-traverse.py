class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        d = defaultdict(list)

        for i in range(m):
            for j in range(n):
                d[i+j].append(mat[i][j])
        
        store = []
        
        for i in range(m + n - 1):
            if i % 2 == 0:
                d[i].reverse()
            store.extend(d[i])
        
        return store
