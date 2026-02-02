class Solution:
    def largestEven(self, s: str) -> str:
        l = list(s)
        if int(''.join(l)) % 2 == 0:
            return ''.join(l)
        for i in range(len(l)-1,-1,-1):
            if int(l[i]) % 2 != 0:
                l.pop(i)
            else:
                return ''.join(l)
        return ''.join(l)