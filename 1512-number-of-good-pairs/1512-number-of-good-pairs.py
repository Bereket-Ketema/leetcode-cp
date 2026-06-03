from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums):
        c = Counter(nums)
        ans = 0

        for v in c.values():
            ans += v * (v - 1) // 2

        return ans