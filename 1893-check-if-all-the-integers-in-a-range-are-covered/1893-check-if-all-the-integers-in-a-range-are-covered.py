class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for l, r in ranges:
            if l > left:
                return False
            if r >= left:
                left = r + 1
            if left > right:
                return True
        return left > right