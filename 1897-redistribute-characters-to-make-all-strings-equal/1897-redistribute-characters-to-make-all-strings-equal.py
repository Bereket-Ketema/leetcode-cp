from collections import Counter

class Solution:
    def makeEqual(self, words):
        c = Counter()
        
        for w in words:
            c += Counter(w)
        
        n = len(words)
        
        return all(v % n == 0 for v in c.values())