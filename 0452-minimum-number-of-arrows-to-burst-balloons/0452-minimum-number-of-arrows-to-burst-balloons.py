class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        left, right = 0, 1
        count = 0
        size = len(points)
        count = 1
        arrow = points[0][1]

        for i in range(1, size):
            if points[i][0] <= arrow:
                continue
            else:
                count += 1
                arrow = points[i][1]

        return count

