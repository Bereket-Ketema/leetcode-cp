class Solution:
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split()
        
        for i, w in enumerate(words, 1):
            if w.startswith(searchWord):
                return i
        
        return -1