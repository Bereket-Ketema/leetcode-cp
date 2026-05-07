from collections import deque

class Solution:
    def minFlips(self, mat):
        m,n = len(mat), len(mat[0])

        start = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    start |= 1<<(i*n+j)

        q = deque([(start,0)])
        vis = {start}

        while q:
            state,d = q.popleft()

            if state == 0:
                return d

            for i in range(m):
                for j in range(n):
                    nxt = state

                    for r,c in [(i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if 0<=r<m and 0<=c<n:
                            nxt ^= 1<<(r*n+c)

                    if nxt not in vis:
                        vis.add(nxt)
                        q.append((nxt,d+1))

        return -1