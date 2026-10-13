from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(x * x for x in nums)
        m = len(sq) // 2
        return sum(sq[m:]) - sum(sq[:m])