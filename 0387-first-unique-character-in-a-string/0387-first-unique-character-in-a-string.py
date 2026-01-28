class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]] = 1
        for k,v in d.items():
            if v ==1:
                return s.index(k)
        return -1