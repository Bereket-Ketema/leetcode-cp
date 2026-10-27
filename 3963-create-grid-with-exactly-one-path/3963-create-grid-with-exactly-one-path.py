from typing import List

class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        grid = [['#' for _ in range(n)] for _ in range(m)]

        for j in range(n):
            grid[0][j] = '.'

        for i in range(1, m):
            grid[i][n - 1] = '.'

        return ["".join(row) for row in grid]