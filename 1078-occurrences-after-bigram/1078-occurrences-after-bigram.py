class Solution:
    def findOcurrences(self, text, first, second):
        w = text.split()
        return [w[i+2] for i in range(len(w)-2) if w[i]==first and w[i+1]==second]