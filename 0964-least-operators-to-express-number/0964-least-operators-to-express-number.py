class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos = neg = 0
        k = 0
        
        while target:
            target, r = divmod(target, x)
            
            if k == 0:
                pos = r * 2
                neg = (x - r) * 2
            else:
                pos2 = min(r * k + pos, (r + 1) * k + neg)
                neg2 = min((x - r) * k + pos, (x - r - 1) * k + neg)
                pos, neg = pos2, neg2
            
            k += 1
        
        return min(pos, neg + k) - 1