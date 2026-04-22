class Solution:
    def commonChars(self, words):
        freq = Counter(words[0])
        
        for word in words[1:]:
            freq &= Counter(word)
        
        return list(freq.elements())