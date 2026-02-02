class Solution:
    def largestEven(self, s: str) -> str:
        if int(s) % 2 == 0:
            return s
        for i in range(len(s)-1,-2,-1):
            if int(s[i]) % 2 == 0:
                return s[:i+1]     
        return ''