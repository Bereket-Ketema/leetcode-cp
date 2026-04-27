class Solution:
    def knightProbability(self, n, k, row, col):
        moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        
        dp = [[0]*n for _ in range(n)]
        dp[row][col] = 1
        
        for _ in range(k):
            new = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if dp[i][j]:
                        for dx, dy in moves:
                            ni, nj = i+dx, j+dy
                            if 0 <= ni < n and 0 <= nj < n:
                                new[ni][nj] += dp[i][j] / 8
            dp = new
        
        return sum(map(sum, dp))