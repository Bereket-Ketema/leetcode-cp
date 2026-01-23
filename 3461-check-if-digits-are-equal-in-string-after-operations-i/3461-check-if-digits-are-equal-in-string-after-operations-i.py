class Solution:
    def hasSameDigits(self, s: str) -> bool:
        k = list(map(int,s))
        for i in range(len(s)-2):
            for j in range(len(s)-1-i):
                k[j]=(k[j] + k[j+1]) % 10
        return k[0] == k[1]

