class Solution:
    def modifyString(self, s):
        s = list(s)

        for i in range(len(s)):
            if s[i] == '?':
                for ch in "abc":
                    prev = s[i-1] if i > 0 else ''
                    nxt = s[i+1] if i < len(s)-1 else ''
                    if ch != prev and ch != nxt:
                        s[i] = ch
                        break

        return "".join(s)