class Solution:
    def findLUSlength(self, strs):
        def is_subseq(a, b):
            i = 0
            for c in b:
                if i < len(a) and a[i] == c:
                    i += 1
            return i == len(a)
        
        strs.sort(key=len, reverse=True)
        
        for i, s in enumerate(strs):
            if all(not is_subseq(s, strs[j]) for j in range(len(strs)) if i != j):
                return len(s)
        
        return -1