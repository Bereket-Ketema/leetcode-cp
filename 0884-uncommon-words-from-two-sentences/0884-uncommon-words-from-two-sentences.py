from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1, s2):
        c = Counter((s1 + " " + s2).split())
        return [w for w,v in c.items() if v == 1]