class Solution:
    def countConsistentStrings(self, allowed, words):
        allowed = set(allowed)
        ans = 0

        for word in words:
            ok = True
            for ch in word:
                if ch not in allowed:
                    ok = False
                    break
            if ok:
                ans += 1

        return ans