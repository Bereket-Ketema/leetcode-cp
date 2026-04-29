class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        
        def can(k):
            return sum((p + k - 1) // k for p in piles) <= h
        
        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        
        return left