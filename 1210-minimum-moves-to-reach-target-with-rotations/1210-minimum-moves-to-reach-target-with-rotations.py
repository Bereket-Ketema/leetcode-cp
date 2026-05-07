from collections import deque

class Solution:
    def minimumMoves(self, grid):
        n = len(grid)
        q = deque([(0,0,0,0)])
        vis = {(0,0,0)}

        while q:
            r,c,pos,d = q.popleft()

            if (r,c,pos) == (n-1,n-2,0):
                return d

            if pos == 0:
                if c+2<n and grid[r][c+2]==0 and (r,c+1,0) not in vis:
                    vis.add((r,c+1,0))
                    q.append((r,c+1,0,d+1))

                if r+1<n and grid[r+1][c]==0 and grid[r+1][c+1]==0:
                    if (r+1,c,0) not in vis:
                        vis.add((r+1,c,0))
                        q.append((r+1,c,0,d+1))

                    if (r,c,1) not in vis:
                        vis.add((r,c,1))
                        q.append((r,c,1,d+1))

            else:
                if r+2<n and grid[r+2][c]==0 and (r+1,c,1) not in vis:
                    vis.add((r+1,c,1))
                    q.append((r+1,c,1,d+1))

                if c+1<n and grid[r][c+1]==0 and grid[r+1][c+1]==0:
                    if (r,c+1,1) not in vis:
                        vis.add((r,c+1,1))
                        q.append((r,c+1,1,d+1))

                    if (r,c,0) not in vis:
                        vis.add((r,c,0))
                        q.append((r,c,0,d+1))

        return -1