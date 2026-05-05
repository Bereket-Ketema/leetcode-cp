import random
import math

class Solution:
    def __init__(self, radius, x_center, y_center):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        angle = random.random() * 2 * math.pi
        dist = math.sqrt(random.random()) * self.r

        return [
            self.x + dist * math.cos(angle),
            self.y + dist * math.sin(angle)
        ]
# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()