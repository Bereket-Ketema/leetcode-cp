class Solution:
    def pushDominoes(self, dominoes):
        s = "L" + dominoes + "R"
        res = []
        i = 0
        
        for j in range(1,len(s)):
            if s[j] == '.':
                continue
            
            mid = j-i-1
            
            if i:
                res.append(s[i])
            
            if s[i] == s[j]:
                res.append(s[i]*mid)
            elif s[i]=='L' and s[j]=='R':
                res.append("."*mid)
            else:
                res.append("R"*(mid//2))
                if mid%2:
                    res.append(".")
                res.append("L"*(mid//2))
            
            i = j
        
        return "".join(res)