import random

class Solution:

    def __init__(self, m, n):
        self.m, self.n = m, n
        self.map = {}
        self.total = m * n

    def flip(self):
        r = random.randint(0, self.total - 1)
        self.total -= 1
        
        x = self.map.get(r, r)
        self.map[r] = self.map.get(self.total, self.total)
        
        return [x // self.n, x % self.n]

    def reset(self):
        self.map.clear()
        self.total = self.m * self.n