class Solution:
    def containVirus(self, grid):
        m, n = len(grid), len(grid[0])
        res = 0

        while True:
            visited = [[0]*n for _ in range(m)]
            regions = []
            frontiers = []
            walls = []

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        stack = [(i, j)]
                        region = []
                        frontier = set()
                        wall = 0
                        visited[i][j] = 1

                        while stack:
                            x, y = stack.pop()
                            region.append((x, y))
                            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                                nx, ny = x+dx, y+dy
                                if 0 <= nx < m and 0 <= ny < n:
                                    if grid[nx][ny] == 0:
                                        frontier.add((nx, ny))
                                        wall += 1
                                    elif grid[nx][ny] == 1 and not visited[nx][ny]:
                                        visited[nx][ny] = 1
                                        stack.append((nx, ny))

                        regions.append(region)
                        frontiers.append(frontier)
                        walls.append(wall)

            if not regions:
                break

            idx = max(range(len(frontiers)), key=lambda i: len(frontiers[i]))
            if len(frontiers[idx]) == 0:
                break

            res += walls[idx]

            for x, y in regions[idx]:
                grid[x][y] = -1

            for i in range(len(regions)):
                if i == idx:
                    continue
                for x, y in frontiers[i]:
                    grid[x][y] = 1

        return res