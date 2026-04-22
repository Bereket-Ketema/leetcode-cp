class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal <= 0:
            return True
        
        total = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
        if total < desiredTotal:
            return False
        
        memo = {}
        
        def dfs(used, remaining):
            if used in memo:
                return memo[used]
            
            for i in range(1, maxChoosableInteger + 1):
                if not (used >> i) & 1:
                    if i >= remaining or not dfs(used | (1 << i), remaining - i):
                        memo[used] = True
                        return True
            
            memo[used] = False
            return False
        
        return dfs(0, desiredTotal)