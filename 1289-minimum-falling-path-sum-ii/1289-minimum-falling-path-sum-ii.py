class Solution:
    def minFallingPathSum(self, grid):
        n=len(grid)
        for i in range(1,n):
            m1,m2=sorted([(grid[i-1][j],j) for j in range(n)])[:2]
            for j in range(n):
                grid[i][j]+= m1[0] if j!=m1[1] else m2[0]
        return min(grid[-1])