class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        right = [0] * n
        down = [0] * n
        right[0] = down[0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                a = right[j - 1] if j > 0 else 0
                b = down[j] if i > 0 else 0
                total = (a + b) % MOD
                if i == m - 1 and j == n - 1:
                    return total
                if grid[i][j] == 0:
                    right[j] = total
                    down[j] = total
                else:
                    right[j] = b
                    down[j] = a
        return 0