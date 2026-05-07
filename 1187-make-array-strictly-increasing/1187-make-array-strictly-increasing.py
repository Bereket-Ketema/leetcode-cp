from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2 = sorted(set(arr2))
        dp = {-1: 0}

        for x in arr1:
            new = {}

            for prev, ops in dp.items():
                if x > prev:
                    new[x] = min(new.get(x, float('inf')), ops)

                idx = bisect_right(arr2, prev)

                if idx < len(arr2):
                    val = arr2[idx]
                    new[val] = min(new.get(val, float('inf')), ops+1)

            dp = new

        return min(dp.values()) if dp else -1