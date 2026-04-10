class Solution:
    def orderlyQueue(self, s, k):
        if k > 1:
            return ''.join(sorted(s))
        
        res = s
        for i in range(len(s)):
            res = min(res, s[i:] + s[:i])
        
        return res