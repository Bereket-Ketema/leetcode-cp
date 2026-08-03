class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0

        for a in range(min(limit, n) + 1):
            for b in range(min(limit, n - a) + 1):
                c = n - a - b
                if 0 <= c <= limit:
                    ans += 1

        return ans