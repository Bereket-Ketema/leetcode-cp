import random
import bisect

class Solution:
    def __init__(self, w):
        self.pre = []
        s = 0
        
        for x in w:
            s += x
            self.pre.append(s)

    def pickIndex(self):
        target = random.randint(1, self.pre[-1])
        return bisect.bisect_left(self.pre, target)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()