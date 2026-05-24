class Solution:
    def numRookCaptures(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rx, ry = i, j
        
        ans = 0
        
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            x,y = rx, ry
            
            while 0 <= x+dx < 8 and 0 <= y+dy < 8:
                x += dx
                y += dy
                
                if board[x][y] == 'B':
                    break
                
                if board[x][y] == 'p':
                    ans += 1
                    break
        
        return ans