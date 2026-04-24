class Solution:
    def updateBoard(self, board, click):
        m, n = len(board), len(board[0])
        x, y = click
        
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        def dfs(i, j):
            if board[i][j] != 'E':
                return
            
            mines = 0
            for dx, dy in directions:
                ni, nj = i+dx, j+dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                    mines += 1
            
            if mines > 0:
                board[i][j] = str(mines)
            else:
                board[i][j] = 'B'
                for dx, dy in directions:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < m and 0 <= nj < n:
                        dfs(ni, nj)
        
        dfs(x, y)
        return board