class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        curr = []
        curr_len = 0
        
        for word in words:
            if curr_len + len(word) + len(curr) > maxWidth:
                spaces = maxWidth - curr_len
                gaps = len(curr) - 1
                
                if gaps == 0:
                    line = curr[0] + ' ' * spaces
                else:
                    space_each = spaces // gaps
                    extra = spaces % gaps
                    
                    line = ''
                    for i in range(gaps):
                        line += curr[i]
                        line += ' ' * (space_each + (1 if i < extra else 0))
                    line += curr[-1]
                
                res.append(line)
                curr = []
                curr_len = 0
            
            curr.append(word)
            curr_len += len(word)
        
        last_line = ' '.join(curr)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res