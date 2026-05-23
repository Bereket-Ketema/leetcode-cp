class Solution:
    def minTaps(self, n, ranges):
        maxReach = [0]*(n+1)
        
        for i,r in enumerate(ranges):
            left = max(0, i-r)
            right = min(n, i+r)
            
            maxReach[left] = max(maxReach[left], right)
        
        taps = 0
        curEnd = 0
        far = 0
        
        for i in range(n):
            far = max(far, maxReach[i])
            
            if i == far:
                return -1
            
            if i == curEnd:
                taps += 1
                curEnd = far
        
        return taps