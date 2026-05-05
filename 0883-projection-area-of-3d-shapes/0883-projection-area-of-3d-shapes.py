class Solution:
    def projectionArea(self, grid):
        top = sum(v > 0 for row in grid for v in row)
        front = sum(max(row) for row in grid)
        side = sum(max(col) for col in zip(*grid))
        return top + front + side