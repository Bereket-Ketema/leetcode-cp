## 51. N-queen
class Solution:
    def solveNQueens(self, n: int):
        cols = [False] * n
        posDiag = [False] * (2*n - 1) # r - c
        negDiag = [False] * (2*n - 1) # r + c
        
        board = [["."] * n for _ in range(n)]
        result = []
        
        def backtrack(r):
            # basecase
            if r == n:
                result.append(["".join(row) for row in board])
                return
            
            # operation 
            for c in range(n):
                posD = r - c
                negD = r + c
                
                if cols[c] or posDiag[posD] or negDiag[negD]: # ignore cell
                    continue
                 
                cols[c] = posDiag[posD] = negDiag[negD] = True
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                cols[c] = posDiag[posD] = negDiag[negD] = False
                board[r][c] = "."
                
        backtrack(0)
        return result
                
                
                