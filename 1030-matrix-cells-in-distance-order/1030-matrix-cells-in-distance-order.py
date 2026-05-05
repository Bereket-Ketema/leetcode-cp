class Solution:
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        res = []
        
        for i in range(rows):
            for j in range(cols):
                dist = abs(i-rCenter) + abs(j-cCenter)
                res.append((dist, i, j))
        
        res.sort()
        return [[i,j] for _,i,j in res]