from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums):
        cnt = Counter(nums)
        return max(cnt.values()) <= 2