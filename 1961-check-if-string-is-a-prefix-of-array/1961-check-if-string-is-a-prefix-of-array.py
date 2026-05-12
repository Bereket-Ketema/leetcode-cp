class Solution:
    def isPrefixString(self, s, words):
        cur = ""

        for w in words:
            cur += w
            if cur == s:
                return True
            if len(cur) > len(s):
                return False

        return False