class Solution:
    def hitBricks(self, grid, hits):
        m, n = len(grid), len(grid[0])
        
        def index(x, y): return x * n + y
        
        parent = list(range(m*n+1))
        size = [1]*(m*n+1)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx
                size[rx] += size[ry]
        
        copy = [row[:] for row in grid]
        for x,y in hits:
            copy[x][y] -= 1
        
        roof = m*n
        
        for i in range(m):
            for j in range(n):
                if copy[i][j] == 1:
                    if i == 0:
                        union(index(i,j), roof)
                    for dx,dy in [(1,0),(0,1)]:
                        ni,nj = i+dx,j+dy
                        if 0<=ni<m and 0<=nj<n and copy[ni][nj]==1:
                            union(index(i,j), index(ni,nj))
        
        res = []
        for x,y in reversed(hits):
            if grid[x][y] == 0:
                res.append(0)
                continue
            
            before = size[find(roof)]
            copy[x][y] = 1
            
            if x == 0:
                union(index(x,y), roof)
            
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni,nj = x+dx,y+dy
                if 0<=ni<m and 0<=nj<n and copy[ni][nj]==1:
                    union(index(x,y), index(ni,nj))
            
            after = size[find(roof)]
            res.append(max(0, after - before - 1))
        
        return res[::-1]