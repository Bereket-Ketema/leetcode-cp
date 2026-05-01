class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        index = 2
        area = {}
        
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=n or grid[i][j]!=1:
                return 0
            grid[i][j] = index
            return 1 + dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[index] = dfs(i,j)
                    index += 1
        
        res = max(area.values() or [0])
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    total = 1
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        ni,nj = i+dx,j+dy
                        if 0<=ni<n and 0<=nj<n and grid[ni][nj] > 1:
                            seen.add(grid[ni][nj])
                    for idx in seen:
                        total += area[idx]
                    res = max(res, total)
        
        return res