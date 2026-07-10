class Solution:
    def removeAnagrams(self, words):
        ans = []
        
        for word in words:
            if not ans or sorted(word) != sorted(ans[-1]):
                ans.append(word)
        
        return ans