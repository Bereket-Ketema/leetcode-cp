class Solution:
    def minDays(self, grid):
        m,n=len(grid),len(grid[0])
        
        def count():
            vis=set()
            islands=0
            
            def dfs(i,j):
                if i<0 or j<0 or i>=m or j>=n or grid[i][j]==0 or (i,j) in vis:
                    return
                vis.add((i,j))
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    dfs(i+dx,j+dy)
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] and (i,j) not in vis:
                        islands+=1
                        dfs(i,j)
            return islands
        
        if count()!=1:
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    grid[i][j]=0
                    if count()!=1:
                        return 1
                    grid[i][j]=1
        return 2