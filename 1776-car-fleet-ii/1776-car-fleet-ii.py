class Solution:
    def getCollisionTimes(self, cars):
        n = len(cars)
        ans = [-1]*n
        stack = []
        
        for i in range(n-1,-1,-1):
            p,s = cars[i]
            
            while stack:
                j = stack[-1]
                p2,s2 = cars[j]
                
                if s <= s2:
                    stack.pop()
                    continue
                
                t = (p2-p)/(s-s2)
                
                if ans[j] == -1 or t <= ans[j]:
                    break
                
                stack.pop()
            
            if stack:
                j = stack[-1]
                ans[i] = (cars[j][0]-p)/(s-cars[j][1])
            
            stack.append(i)
        
        return ans