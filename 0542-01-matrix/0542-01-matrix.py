from collections import deque

class Solution:
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = float('inf')
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n:
                    if mat[nx][ny] > mat[x][y] + 1:
                        mat[nx][ny] = mat[x][y] + 1
                        q.append((nx, ny))
        
        return mat