from collections import deque

class Solution:
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        n = len(boxes)
        
        p = [0]*(n+1)
        w = [0]*(n+1)
        neg = [0]*(n+1)
        
        for i in range(n):
            p[i+1] = boxes[i][0]
            w[i+1] = w[i] + boxes[i][1]
        
        for i in range(2,n+1):
            neg[i] = neg[i-1] + (p[i] != p[i-1])
        
        dp = [0]*(n+1)
        dq = deque([0])
        
        for i in range(1,n+1):
            while dq and (
                i-dq[0] > maxBoxes or
                w[i]-w[dq[0]] > maxWeight
            ):
                dq.popleft()
            
            dp[i] = dp[dq[0]] + neg[i] - neg[dq[0]+1] + 2
            
            if i != n:
                val = dp[i] - neg[i+1]
                
                while dq and (
                    dp[dq[-1]] - neg[dq[-1]+1]
                    >= val
                ):
                    dq.pop()
                
                dq.append(i)
        
        return dp[n]