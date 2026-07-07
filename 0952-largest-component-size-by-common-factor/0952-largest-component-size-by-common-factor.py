from collections import Counter
import math
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.p = list(range(n))
    
    def union(self, a: int, b: int):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.p[pa] = pb
    
    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_val = max(nums)
        uf = UnionFind(max_val + 1)
        
        for v in nums:
            if v == 1:
                continue
            i = 2
            while i * i <= v:
                if v % i == 0:
                    uf.union(v, i)
                    uf.union(v, v // i)
                i += 1
            # Handle prime case if needed, but the loop covers it
        
        # Count sizes of components for numbers in nums
        count = Counter(uf.find(v) for v in nums)
        return max(count.values()) if count else 0