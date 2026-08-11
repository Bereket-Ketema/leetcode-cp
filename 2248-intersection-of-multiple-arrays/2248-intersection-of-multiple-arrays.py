from collections import Counter

class Solution:
    def intersection(self, nums):
        n = len(nums)
        count = Counter()

        for arr in nums:
            for x in set(arr):
                count[x] += 1

        return sorted(
            x for x in count
            if count[x] == n
        )