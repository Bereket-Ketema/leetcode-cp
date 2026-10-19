from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller = sum(1 for x in nums if x < target)
        count = sum(1 for x in nums if x == target)
        return list(range(smaller, smaller + count))