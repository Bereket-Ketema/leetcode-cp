class Solution:
    def findLongestWord(self, s, dictionary):
        dictionary.sort(key=lambda x: (-len(x), x))
        
        def ok(word):
            i = 0
            for c in s:
                if i < len(word) and c == word[i]:
                    i += 1
            return i == len(word)
        
        for w in dictionary:
            if ok(w):
                return w
        return ""