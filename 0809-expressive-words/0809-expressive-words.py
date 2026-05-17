class Solution:
    def expressiveWords(self, s, words):
        def check(word):
            i = j = 0
            
            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    return False
                
                i1 = i
                while i < len(s) and s[i] == s[i1]:
                    i += 1
                
                j1 = j
                while j < len(word) and word[j] == word[j1]:
                    j += 1
                
                len1 = i - i1
                len2 = j - j1
                
                if len1 < len2:
                    return False
                if len1 != len2 and len1 < 3:
                    return False
            
            return i == len(s) and j == len(word)
        
        return sum(check(w) for w in words)