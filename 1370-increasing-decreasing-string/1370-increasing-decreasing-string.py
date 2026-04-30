class Solution:
    def sortString(self, s):
        from collections import Counter
        count = Counter(s)
        res = []
        
        while count:
            for c in sorted(count):
                res.append(c)
                count[c] -= 1
                if count[c] == 0:
                    del count[c]
            
            for c in sorted(count, reverse=True):
                res.append(c)
                count[c] -= 1
                if count[c] == 0:
                    del count[c]
        
        return ''.join(res)