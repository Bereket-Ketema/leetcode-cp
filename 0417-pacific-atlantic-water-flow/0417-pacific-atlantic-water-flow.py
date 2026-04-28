class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        
        m, n = len(heights), len(heights[0])
        pac = set()
        atl = set()
        
        def dfs(i, j, visited):
            visited.add((i, j))
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = i+dx, j+dy
                if 0 <= ni < m and 0 <= nj < n:
                    if (ni, nj) not in visited and heights[ni][nj] >= heights[i][j]:
                        dfs(ni, nj, visited)
        
        for i in range(m):
            dfs(i, 0, pac)
            dfs(i, n-1, atl)
        
        for j in range(n):
            dfs(0, j, pac)
            dfs(m-1, j, atl)
        
        return list(pac & atl)