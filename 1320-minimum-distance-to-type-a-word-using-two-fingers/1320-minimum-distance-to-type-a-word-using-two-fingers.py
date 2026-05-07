from functools import lru_cache

class Solution:
    def minimumDistance(self, word):
        def pos(c):
            x = ord(c)-65
            return x//6, x%6

        def dist(a,b):
            if a == -1:
                return 0

            x1,y1 = pos(chr(a+65))
            x2,y2 = pos(chr(b+65))
            return abs(x1-x2)+abs(y1-y2)

        @lru_cache(None)
        def dp(i,f1,f2):
            if i == len(word):
                return 0

            cur = ord(word[i])-65

            return min(
                dist(f1,cur)+dp(i+1,cur,f2),
                dist(f2,cur)+dp(i+1,f1,cur)
            )

        return dp(0,-1,-1)