class Solution:
    def numMagicSquaresInside(self, grid):
        def is_magic(i, j):
            nums = [grid[i+x][j+y] for x in range(3) for y in range(3)]
            if sorted(nums) != list(range(1,10)):
                return False
            
            rows = [sum(grid[i+r][j+c] for c in range(3)) for r in range(3)]
            cols = [sum(grid[i+r][j+c] for r in range(3)) for c in range(3)]
            diag1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
            diag2 = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
            
            return len(set(rows + cols + [diag1, diag2])) == 1
        
        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if is_magic(i, j):
                    count += 1
        
        return count