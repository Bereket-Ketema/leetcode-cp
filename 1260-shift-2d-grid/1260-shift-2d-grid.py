class Solution:
    def shiftGrid(self, grid, k):
        m,n = len(grid), len(grid[0])
        
        arr = []
        for row in grid:
            arr.extend(row)
        
        k %= (m*n)
        arr = arr[-k:] + arr[:-k]
        
        res = []
        idx = 0
        
        for i in range(m):
            row = []
            for j in range(n):
                row.append(arr[idx])
                idx += 1
            res.append(row)
        
        return res