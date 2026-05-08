from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid):
        m,n = len(grid), len(grid[0])
        keys = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    sx,sy = i,j
                elif grid[i][j].islower():
                    keys = max(keys, ord(grid[i][j])-97+1)

        target = (1<<keys)-1
        q = deque([(sx,sy,0,0)])
        vis = {(sx,sy,0)}

        while q:
            x,y,mask,dist = q.popleft()

            if mask == target:
                return dist

            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = x+dx,y+dy

                if 0<=nx<m and 0<=ny<n:
                    c = grid[nx][ny]

                    if c == '#':
                        continue

                    nmask = mask

                    if c.islower():
                        nmask |= (1<<(ord(c)-97))

                    if c.isupper() and not (mask & (1<<(ord(c)-65))):
                        continue

                    if (nx,ny,nmask) not in vis:
                        vis.add((nx,ny,nmask))
                        q.append((nx,ny,nmask,dist+1))

        return -1