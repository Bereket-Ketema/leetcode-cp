from functools import lru_cache

class Solution:
    def findGoodStrings(self, n, s1, s2, evil):
        MOD = 10**9+7
        
        lps = [0]*len(evil)
        j = 0
        
        for i in range(1,len(evil)):
            while j and evil[i] != evil[j]:
                j = lps[j-1]
            if evil[i] == evil[j]:
                j += 1
                lps[i] = j
        
        @lru_cache(None)
        def dfs(i, matched, low, high):
            if matched == len(evil):
                return 0
            if i == n:
                return 1
            
            lo = s1[i] if low else 'a'
            hi = s2[i] if high else 'z'
            
            ans = 0
            
            for ch in range(ord(lo), ord(hi)+1):
                c = chr(ch)
                
                k = matched
                while k and evil[k] != c:
                    k = lps[k-1]
                
                if evil[k] == c:
                    k += 1
                
                ans += dfs(
                    i+1,
                    k,
                    low and c == lo,
                    high and c == hi
                )
            
            return ans % MOD
        
        return dfs(0,0,True,True)