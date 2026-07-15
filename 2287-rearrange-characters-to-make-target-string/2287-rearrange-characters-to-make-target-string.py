from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cntS = Counter(s)
        cntT = Counter(target)

        ans = float('inf')

        for ch in cntT:
            ans = min(ans, cntS[ch] // cntT[ch])

        return ans