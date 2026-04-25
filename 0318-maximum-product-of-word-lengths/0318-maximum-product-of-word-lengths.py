class Solution:
    def maxProduct(self, words):
        masks = []
        for w in words:
            mask = 0
            for c in w:
                mask |= 1 << (ord(c) - ord('a'))
            masks.append((mask, len(w)))
        
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if masks[i][0] & masks[j][0] == 0:
                    res = max(res, masks[i][1] * masks[j][1])
        
        return res