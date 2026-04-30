class Solution:
    def luckyNumbers(self, matrix):
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]
        
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == row_min[i] == col_max[j]:
                    res.append(matrix[i][j])
        
        return res