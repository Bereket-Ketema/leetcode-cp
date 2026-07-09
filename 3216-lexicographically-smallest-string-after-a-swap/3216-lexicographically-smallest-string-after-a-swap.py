class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(s)

        for i in range(len(s) - 1):
            if s[i] > s[i + 1] and (int(s[i]) % 2) == (int(s[i + 1]) % 2):
                s[i], s[i + 1] = s[i + 1], s[i]
                break

        return "".join(s)