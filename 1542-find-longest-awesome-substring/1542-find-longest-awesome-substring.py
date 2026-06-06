class Solution:
    def longestAwesome(self, s):
        pos = {0: -1}
        mask = 0
        ans = 0

        for i, ch in enumerate(s):
            mask ^= 1 << int(ch)

            if mask in pos:
                ans = max(ans, i - pos[mask])
            else:
                pos[mask] = i

            for b in range(10):
                cur = mask ^ (1 << b)
                if cur in pos:
                    ans = max(ans, i - pos[cur])

        return ans