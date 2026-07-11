class Solution:
    def prefixCount(self, words, pref):
        ans = 0
        
        for word in words:
            if word.startswith(pref):
                ans += 1
        
        return ans