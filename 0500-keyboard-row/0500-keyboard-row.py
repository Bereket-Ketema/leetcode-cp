class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        keep = []
        for word in range(len(words)):
            if words[word][0].lower() in first:
                store = first
            elif words[word][0].lower() in second:
                store = second
            else:
                store = third
            l = 0
            while l < len(words[word]):
                if words[word][l].lower() not in store:
                    break
                if l == len(words[word])-1:
                    keep.append(words[word])
                l+=1
        return keep