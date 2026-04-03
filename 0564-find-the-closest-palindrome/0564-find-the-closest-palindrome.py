class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)
        
        candidates = set()
        candidates.add(str(10**(length - 1) - 1))  
        candidates.add(str(10**length + 1))      
        
        prefix = int(n[:(length + 1)//2])
        
        for diff in [-1, 0, 1]:
            p = str(prefix + diff)
            
            if length % 2 == 0:
                palindrome = p + p[::-1]
            else:
                palindrome = p + p[:-1][::-1]
            
            candidates.add(palindrome)
        
        candidates.discard(n)
        
        closest = None
        
        for cand in candidates:
            if cand == "":
                continue
            val = int(cand)
            
            if closest is None:
                closest = val
            else:
                if abs(val - num) < abs(closest - num) or \
                   (abs(val - num) == abs(closest - num) and val < closest):
                    closest = val
        
        return str(closest)