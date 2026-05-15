class Solution:
    def findKthNumber(self, m, n, k):
        def count(x):
            total = 0
            for i in range(1, m+1):
                total += min(x // i, n)
            return total

        l, r = 1, m * n

        while l < r:
            mid = (l + r) // 2
            if count(mid) >= k:
                r = mid
            else:
                l = mid + 1

        return l