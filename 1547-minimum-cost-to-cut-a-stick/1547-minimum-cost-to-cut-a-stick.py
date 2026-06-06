from functools import lru_cache

class Solution:
    def minCost(self, n, cuts):
        cuts.sort()
        cuts = [0] + cuts + [n]

        @lru_cache(None)
        def dp(l, r):
            if r - l <= 1:
                return 0

            res = float('inf')

            for k in range(l + 1, r):
                res = min(
                    res,
                    cuts[r] - cuts[l] +
                    dp(l, k) +
                    dp(k, r)
                )

            return res

        return dp(0, len(cuts) - 1)