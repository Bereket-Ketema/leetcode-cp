from collections import deque

class Solution:
    def cutOffTree(self, forest):
        if not forest or not forest[0]:
            return -1
        
        rows, cols = len(forest), len(forest[0])
        trees = sorted((h, r, c) for r, row in enumerate(forest) 
                       for c, h in enumerate(row) if h > 1)
        
        def bfs(sr, sc, tr, tc):
            visited = [[False]*cols for _ in range(rows)]
            queue = deque([(sr, sc, 0)])
            visited[sr][sc] = True
            
            while queue:
                r, c, steps = queue.popleft()
                if r == tr and c == tc:
                    return steps
                
                for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and forest[nr][nc] != 0:
                        visited[nr][nc] = True
                        queue.append((nr, nc, steps + 1))
            return -1
        
        sr = sc = total_steps = 0
        
        for _, tr, tc in trees:
            steps = bfs(sr, sc, tr, tc)
            if steps == -1:
                return -1
            total_steps += steps
            sr, sc = tr, tc
        
        return total_steps