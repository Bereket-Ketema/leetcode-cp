class Solution:
    def surfaceArea(self, grid):
        n = len(grid)
        ans = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    ans += grid[i][j]*4 + 2
                    
                    if i > 0:
                        ans -= 2*min(grid[i][j], grid[i-1][j])
                    if j > 0:
                        ans -= 2*min(grid[i][j], grid[i][j-1])
        
        return ans