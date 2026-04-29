from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        
        def get_pos(num):
            r, c = divmod(num - 1, n)
            if r % 2:
                c = n - 1 - c
            return n - 1 - r, c
        
        q = deque([(1, 0)])
        visited = {1}
        
        while q:
            num, steps = q.popleft()
            if num == n * n:
                return steps
            
            for i in range(1, 7):
                nxt = num + i
                if nxt > n * n:
                    continue
                r, c = get_pos(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))
        
        return -1