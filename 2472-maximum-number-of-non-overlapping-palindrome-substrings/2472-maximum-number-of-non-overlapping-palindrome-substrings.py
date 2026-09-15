class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        centers = []
        for i in range(n):
            centers.append((i, i))
            centers.append((i, i + 1))

        intervals = []
        for l, r in centers:
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    intervals.append((l, r))
                    break
                l -= 1
                r += 1

        intervals.sort(key=lambda x: x[1])
        ans = 0
        last_end = -1
        for start, end in intervals:
            if start > last_end:
                ans += 1
                last_end = end

        return ans