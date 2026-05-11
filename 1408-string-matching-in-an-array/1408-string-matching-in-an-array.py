class Solution:
    def stringMatching(self, words):
        res = []
        
        for w in words:
            for x in words:
                if w != x and w in x:
                    res.append(w)
                    break
        
        return res