from collections import Counter

class Solution:
    def mostFrequentEven(self, nums):
        cnt = Counter(x for x in nums if x % 2 == 0)

        if not cnt:
            return -1

        mx = max(cnt.values())

        return min(x for x, f in cnt.items() if f == mx)