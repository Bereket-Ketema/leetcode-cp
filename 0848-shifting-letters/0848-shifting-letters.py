class Solution:
    def shiftingLetters(self, s, shifts):
        total = 0
        shifts = shifts[::-1]
        res = []
        
        for i in range(len(s)-1, -1, -1):
            total = (total + shifts[len(s)-1 - i]) % 26
            new_char = chr((ord(s[i]) - ord('a') + total) % 26 + ord('a'))
            res.append(new_char)
        
        return ''.join(res[::-1])