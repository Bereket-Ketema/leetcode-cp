from math import comb

class Solution:
    def getProbability(self, balls):
        n = len(balls)
        total = sum(balls)
        half = total // 2
        
        fact = [1]*(total+1)
        for i in range(1, total+1):
            fact[i] = fact[i-1]*i
        
        def ways(arr):
            s = sum(arr)
            res = fact[s]
            for x in arr:
                res //= fact[x]
            return res
        
        good = 0
        totalWays = 0
        
        box1 = [0]*n
        
        def dfs(i, cnt1, d1, d2):
            nonlocal good, totalWays
            
            if cnt1 > half:
                return
            
            if i == n:
                if cnt1 == half:
                    box2 = [balls[j]-box1[j] for j in range(n)]
                    
                    w1 = ways(box1)
                    w2 = ways(box2)
                    
                    totalWays += w1*w2
                    
                    if d1 == d2:
                        good += w1*w2
                return
            
            for take in range(balls[i]+1):
                box1[i] = take
                
                dfs(
                    i+1,
                    cnt1+take,
                    d1 + (take > 0),
                    d2 + (balls[i]-take > 0)
                )
        
        dfs(0,0,0,0)
        
        return good / totalWays