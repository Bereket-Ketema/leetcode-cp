import random

class Solution:
    def __init__(self, n, blacklist):
        self.map = {}
        self.bound = n - len(blacklist)
        blacklist_set = set(blacklist)
        
        last = n - 1
        for b in blacklist:
            if b < self.bound:
                while last in blacklist_set:
                    last -= 1
                self.map[b] = last
                last -= 1

    def pick(self):
        x = random.randint(0, self.bound - 1)
        return self.map.get(x, x)