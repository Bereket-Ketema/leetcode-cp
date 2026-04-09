from functools import lru_cache
from collections import Counter

class Solution:
    def minStickers(self, stickers, target):
        m = len(stickers)
        sticker_counts = [Counter(s) for s in stickers]

        @lru_cache(None)
        def dp(remain):
            if not remain:
                return 0
            
            need = Counter(remain)
            res = float('inf')
            
            for sc in sticker_counts:
                if remain[0] not in sc:
                    continue
                
                new_remain = ""
                for c in need:
                    if need[c] > sc[c]:
                        new_remain += c * (need[c] - sc[c])
                
                sub = dp(new_remain)
                if sub != -1:
                    res = min(res, 1 + sub)
            
            return res if res != float('inf') else -1
        
        return dp(target)