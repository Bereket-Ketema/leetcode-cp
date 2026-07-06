class Solution:
    def reformatNumber(self, number):
        s = ""

        for ch in number:
            if ch.isdigit():
                s += ch

        n = len(s)
        ans = []
        i = 0

        while n - i > 4:
            ans.append(s[i:i + 3])
            i += 3

        if n - i == 4:
            ans.append(s[i:i + 2])
            ans.append(s[i + 2:i + 4])
        else:
            ans.append(s[i:])

        return "-".join(ans)