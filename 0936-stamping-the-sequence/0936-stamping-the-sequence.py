class Solution:
    def movesToStamp(self, stamp, target):
        s = list(target)
        stamp = list(stamp)
        
        m, n = len(stamp), len(s)
        res = []
        visited = [False] * (n-m+1)
        stars = 0
        
        def canReplace(pos):
            changed = False
            
            for i in range(m):
                if s[pos+i] == '*':
                    continue
                
                if s[pos+i] != stamp[i]:
                    return False
                
                changed = True
            
            return changed
        
        def doReplace(pos):
            cnt = 0
            
            for i in range(m):
                if s[pos+i] != '*':
                    s[pos+i] = '*'
                    cnt += 1
            
            return cnt
        
        while stars < n:
            done = False
            
            for i in range(n-m+1):
                if not visited[i] and canReplace(i):
                    visited[i] = True
                    stars += doReplace(i)
                    done = True
                    res.append(i)
                    
                    if stars == n:
                        break
            
            if not done:
                return []
        
        return res[::-1]