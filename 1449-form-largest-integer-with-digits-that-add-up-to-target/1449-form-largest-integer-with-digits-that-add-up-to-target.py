class Solution:
    def largestNumber(self, cost, target):
        dp = [""] + [None]*target
        
        for t in range(1,target+1):
            for d in range(9):
                c = cost[d]
                
                if t >= c and dp[t-c] is not None:
                    cand = str(d+1) + dp[t-c]
                    
                    if (dp[t] is None or
                        len(cand) > len(dp[t]) or
                        (len(cand)==len(dp[t]) and cand > dp[t])):
                        dp[t] = cand
        
        return dp[target] if dp[target] else "0"