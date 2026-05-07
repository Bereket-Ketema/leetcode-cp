from collections import deque

class Solution:
    def minCost(self, grid):
        m,n = len(grid), len(grid[0])

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        dq = deque([(0,0,0)])
        vis = set()

        while dq:
            cost,r,c = dq.popleft()

            if (r,c) in vis:
                continue

            vis.add((r,c))

            if (r,c) == (m-1,n-1):
                return cost

            for i,(dr,dc) in enumerate(dirs,1):
                nr,nc = r+dr,c+dc

                if 0<=nr<m and 0<=nc<n:
                    if grid[r][c] == i:
                        dq.appendleft((cost,nr,nc))
                    else:
                        dq.append((cost+1,nr,nc))