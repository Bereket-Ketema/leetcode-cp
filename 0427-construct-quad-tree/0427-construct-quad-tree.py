# Definition for a QuadTree node.
# class Node:
#     def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        def build(r, c, size):
            first = grid[r][c]
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        half = size // 2
                        return Node(
                            True, False,
                            build(r, c, half),
                            build(r, c + half, half),
                            build(r + half, c, half),
                            build(r + half, c + half, half)
                        )
            
            return Node(first == 1, True, None, None, None, None)
        
        return build(0, 0, len(grid))