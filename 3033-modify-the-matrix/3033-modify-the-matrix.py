class Solution:
    def modifiedMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])

        col_max = [0] * n
        for j in range(n):
            col_max[j] = max(matrix[i][j] for i in range(m))

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = col_max[j]

        return matrix