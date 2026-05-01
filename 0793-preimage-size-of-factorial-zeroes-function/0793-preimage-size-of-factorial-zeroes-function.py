class Solution:
    def preimageSizeFZF(self, k):
        def zeta(x):
            res = 0
            while x:
                x //= 5
                res += x
            return res
        
        left, right = 0, 5 * (k + 1)
        while left < right:
            mid = (left + right) // 2
            if zeta(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return 5 if zeta(left) == k else 0