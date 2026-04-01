class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        pos = defaultdict(list)
        for i, ch in enumerate(ring):
            pos[ch].append(i)

        n = len(ring)

        @lru_cache(None)
        def dp(i, k):
            if k == len(key):
                return 0
            
            res = float('inf')
            
            for j in pos[key[k]]:
                dist = abs(i - j)
                step = min(dist, n - dist)
                
                res = min(res, step + 1 + dp(j, k + 1))
            
            return res

        return dp(0, 0)