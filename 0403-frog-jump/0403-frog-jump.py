class Solution:
    def canCross(self, stones):
        dp = {stone: set() for stone in stones}
        dp[stones[0]].add(0)
        
        for stone in stones:
            for k in dp[stone]:
                for step in [k-1, k, k+1]:
                    if step > 0 and stone + step in dp:
                        dp[stone + step].add(step)
        
        return bool(dp[stones[-1]])