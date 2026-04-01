class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [False] * n
        posDiag = [False] * (2 * n - 1)  # r - c + (n-1)
        negDiag = [False] * (2 * n - 1)  # r + c
        
        count = 0
        
        def backtrack(r):
            nonlocal count
            
            # base case
            if r == n:
                count += 1
                return
            
            for c in range(n):
                posD = r - c + (n - 1)
                negD = r + c
                
                if cols[c] or posDiag[posD] or negDiag[negD]:
                    continue
                
                cols[c] = posDiag[posD] = negDiag[negD] = True
                
                backtrack(r + 1)
                
                cols[c] = posDiag[posD] = negDiag[negD] = False
        
        backtrack(0)
        return count