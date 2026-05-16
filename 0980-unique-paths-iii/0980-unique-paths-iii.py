class Solution:
    def uniquePathsIII(self, grid):
        m,n = len(grid), len(grid[0])
        empty = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] >= 0:
                    empty += 1
                if grid[i][j] == 1:
                    sx, sy = i, j
        
        def dfs(x,y,count):
            if grid[x][y] == 2:
                return count == empty
            
            temp = grid[x][y]
            grid[x][y] = -1
            
            res = 0
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] >= 0:
                    res += dfs(nx,ny,count+1)
            
            grid[x][y] = temp
            return res
        
        return dfs(sx,sy,1)