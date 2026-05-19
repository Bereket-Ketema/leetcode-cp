class Solution:
    def countValidWords(self, sentence):
        words = sentence.split()
        ans = 0
        
        for w in words:
            hyphen = 0
            ok = True
            
            for i,ch in enumerate(w):
                if ch.isdigit():
                    ok = False
                    break
                
                if ch in "!.,":  
                    if i != len(w)-1:
                        ok = False
                        break
                
                if ch == '-':
                    hyphen += 1
                    
                    if (hyphen > 1 or
                        i == 0 or
                        i == len(w)-1 or
                        not w[i-1].islower() or
                        not w[i+1].islower()):
                        ok = False
                        break
            
            if ok:
                ans += 1
        
        return ans