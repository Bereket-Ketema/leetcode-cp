class Solution:
    def reorderSpaces(self, text):
        spaces = text.count(' ')
        words = text.split()
        
        if len(words) == 1:
            return words[0] + ' ' * spaces
        
        between = spaces // (len(words) - 1)
        extra = spaces % (len(words) - 1)
        
        return (' ' * between).join(words) + ' ' * extra