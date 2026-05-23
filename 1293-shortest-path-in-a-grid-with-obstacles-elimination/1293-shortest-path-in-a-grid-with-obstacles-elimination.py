from collections import deque

class Solution:
    def shortestPath(self, grid, k):
        m,n = len(grid), len(grid[0])
        
        q = deque([(0,0,k,0)])
        vis = {(0,0,k)}
        
        while q:
            x,y,rem,dist = q.popleft()
            
            if x == m-1 and y == n-1:
                return dist
            
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = x+dx,y+dy
                
                if 0<=nx<m and 0<=ny<n:
                    nr = rem-grid[nx][ny]
                    
                    if nr >= 0 and (nx,ny,nr) not in vis:
                        vis.add((nx,ny,nr))
                        q.append((nx,ny,nr,dist+1))
        
        return -1