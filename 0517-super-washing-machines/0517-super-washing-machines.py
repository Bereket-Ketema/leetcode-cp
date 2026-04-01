class Solution:
    def findMinMoves(self, machines):
        total = sum(machines)
        n = len(machines)
        
        if total % n != 0:
            return -1
        
        avg = total // n
        res = 0
        curr = 0
        
        for m in machines:
            diff = m - avg
            curr += diff
            res = max(res, abs(curr), diff)
        
        return res