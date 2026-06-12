class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = n - 1
        
        pos = time % (2 * cycle)
        
        if pos <= cycle:
            return pos + 1
        
        return n - (pos - cycle)