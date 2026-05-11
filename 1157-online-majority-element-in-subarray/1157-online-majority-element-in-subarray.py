import random
from collections import defaultdict
import bisect

class MajorityChecker:

    def __init__(self, arr):
        self.arr = arr
        self.pos = defaultdict(list)

        for i,x in enumerate(arr):
            self.pos[x].append(i)

    def query(self, left, right, threshold):
        for _ in range(20):
            x = self.arr[random.randint(left,right)]
            lst = self.pos[x]

            cnt = bisect.bisect_right(lst,right) - bisect.bisect_left(lst,left)

            if cnt >= threshold:
                return x

        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)