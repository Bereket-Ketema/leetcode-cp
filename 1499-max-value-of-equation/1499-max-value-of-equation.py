from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points, k):
        dq=deque()
        ans=-10**18
        
        for x,y in points:
            while dq and x-dq[0][0]>k:
                dq.popleft()
            
            if dq:
                ans=max(ans,x+y+dq[0][1])
            
            while dq and dq[-1][1]<=y-x:
                dq.pop()
            
            dq.append((x,y-x))
        
        return ans