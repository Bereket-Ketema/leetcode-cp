from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr):
        res = -1
        
        for h1, h2, m1, m2 in permutations(arr):
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            
            if hour < 24 and minute < 60:
                res = max(res, hour * 60 + minute)
        
        if res == -1:
            return ""
        
        return f"{res//60:02d}:{res%60:02d}"