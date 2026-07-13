class Solution:
    def minTimeToType(self, word: str) -> int:
        cur = 'a'
        ans = 0

        for ch in word:
            diff = abs(ord(ch) - ord(cur))
            ans += min(diff, 26 - diff) + 1
            cur = ch

        return ans