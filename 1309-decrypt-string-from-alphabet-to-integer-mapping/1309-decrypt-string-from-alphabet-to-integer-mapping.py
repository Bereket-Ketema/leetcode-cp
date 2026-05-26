class Solution:
    def freqAlphabets(self, s):
        ans = []
        i = 0
        
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                num = int(s[i:i+2])
                ans.append(chr(num + 96))
                i += 3
            else:
                ans.append(chr(int(s[i]) + 96))
                i += 1
        
        return "".join(ans)