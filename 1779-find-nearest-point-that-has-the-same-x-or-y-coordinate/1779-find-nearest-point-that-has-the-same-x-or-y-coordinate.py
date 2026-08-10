class Solution:
    def nearestValidPoint(self, x, y, points):
        ans = -1
        best = float("inf")

        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                dist = abs(px - x) + abs(py - y)

                if dist < best:
                    best = dist
                    ans = i

        return ans