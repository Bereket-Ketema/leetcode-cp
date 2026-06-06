from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s, k):
        @lru_cache(None)
        def dp(i, k):
            if k < 0:
                return float('inf')

            if i >= len(s) or len(s) - i <= k:
                return 0

            res = dp(i + 1, k - 1)

            cnt = 0
            deleted = 0

            for j in range(i, len(s)):
                if s[j] == s[i]:
                    cnt += 1
                else:
                    deleted += 1

                if deleted > k:
                    break

                add = 1
                if cnt >= 100:
                    add = 4
                elif cnt >= 10:
                    add = 3
                elif cnt >= 2:
                    add = 2

                res = min(res, add + dp(j + 1, k - deleted))

            return res

        return dp(0, k)