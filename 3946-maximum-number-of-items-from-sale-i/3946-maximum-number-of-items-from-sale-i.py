from collections import Counter
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        max_factor = max(f for f, _ in items)
        freq = Counter(f for f, _ in items)
        
        multiples_count = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if f in freq:
                for m in range(f, max_factor + 1, f):
                    multiples_count[f] += freq[m]
                    
        dp = [0] * (budget + 1)
        min_price = min(p for _, p in items)
        
        for f, p in items:
            first_copy_value = multiples_count[f]
            for c in range(budget, p - 1, -1):
                if dp[c - p] + first_copy_value > dp[c]:
                    dp[c] = dp[c - p] + first_copy_value
                    
        ans = 0
        for c in range(budget + 1):
            extra_copies = (budget - c) // min_price
            ans = max(ans, dp[c] + extra_copies)
            
        return ans