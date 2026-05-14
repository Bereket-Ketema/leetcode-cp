from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck):
        vals = Counter(deck).values()
        g = 0
        
        for v in vals:
            g = math.gcd(g, v)
        
        return g >= 2