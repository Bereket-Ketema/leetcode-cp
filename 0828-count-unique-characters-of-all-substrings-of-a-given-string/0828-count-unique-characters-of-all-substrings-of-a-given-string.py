class Solution:
    def uniqueLetterString(self, s):
        index = {c: [-1, -1] for c in set(s)}
        res = 0
        
        for i, ch in enumerate(s):
            k, j = index[ch]
            res += (i - j) * (j - k)
            index[ch] = [j, i]
        
        n = len(s)
        for ch in index:
            k, j = index[ch]
            res += (n - j) * (j - k)
        
        return res