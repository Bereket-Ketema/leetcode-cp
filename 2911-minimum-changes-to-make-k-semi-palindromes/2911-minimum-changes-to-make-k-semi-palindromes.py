from typing import List

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length // 2 + 1):
                if length % d == 0:
                    divisors[length].append(d)
                    
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = float('inf')
                for d in divisors[length]:
                    changes = 0
                    for rem in range(d):
                        left = i + rem
                        right = j - d + 1 + rem
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    if changes < best:
                        best = changes
                cost[i][j] = best
                
        inf = float('inf')
        dp = [[inf] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        
        for parts in range(1, k + 1):
            for end in range(parts * 2, n + 1):
                for prev in range((parts - 1) * 2, end - 1):
                    if dp[parts - 1][prev] != inf:
                        dp[parts][end] = min(dp[parts][end], dp[parts - 1][prev] + cost[prev][end - 1])
                        
        return dp[k][n]