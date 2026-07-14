class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []

        for ch in s:
            if len(ans) >= 2 and ans[-1] == ans[-2] == ch:
                continue
            ans.append(ch)

        return "".join(ans)