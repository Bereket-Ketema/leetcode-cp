class Solution:
    def numSquarefulPerms(self, nums):
        from collections import Counter
        import math
        
        count = Counter(nums)
        
        def dfs(prev, left):
            if left == 0:
                return 1
            res = 0
            for x in count:
                if count[x] and (prev is None or int(math.isqrt(prev+x))**2 == prev+x):
                    count[x] -= 1
                    res += dfs(x, left-1)
                    count[x] += 1
            return res
        
        return dfs(None, len(nums))