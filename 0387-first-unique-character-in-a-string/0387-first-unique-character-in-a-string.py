from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for k,v in d.items():
            if v ==1 :
                return s.index(k)
        return -1