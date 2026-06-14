class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        res = []

        while len(s) > 3:
            res.append(s[-3:])
            s = s[:-3]

        res.append(s)

        return '.'.join(res[::-1])