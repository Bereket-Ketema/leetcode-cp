from collections import deque

class Solution:
    def minPushBox(self, grid):
        m,n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='S':
                    px,py=i,j
                elif grid[i][j]=='B':
                    bx,by=i,j
                elif grid[i][j]=='T':
                    tx,ty=i,j

        q=deque([(bx,by,px,py,0)])
        vis={(bx,by,px,py)}

        def canReach(sx,sy,tx,ty,bx,by):
            dq=deque([(sx,sy)])
            seen={(sx,sy)}

            while dq:
                x,y=dq.popleft()
                if (x,y)==(tx,ty):
                    return True

                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]!='#' and (nx,ny)!=(bx,by) and (nx,ny) not in seen:
                        seen.add((nx,ny))
                        dq.append((nx,ny))
            return False

        while q:
            bx,by,px,py,pushes=q.popleft()

            if (bx,by)==(tx,ty):
                return pushes

            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nbx,nby=bx+dx,by+dy
                reqx,reqy=bx-dx,by-dy

                if not (0<=nbx<m and 0<=nby<n):
                    continue
                if not (0<=reqx<m and 0<=reqy<n):
                    continue
                if grid[nbx][nby]=='#' or grid[reqx][reqy]=='#':
                    continue

                if canReach(px,py,reqx,reqy,bx,by):
                    state=(nbx,nby,bx,by)
                    if state not in vis:
                        vis.add(state)
                        q.append((nbx,nby,bx,by,pushes+1))

        return -1