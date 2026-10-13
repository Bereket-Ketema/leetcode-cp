from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        bit_count = [0] * 31

        for x in nums:
            for b in range(31):
                if (x >> b) & 1:
                    bit_count[b] += 1

        ans = 0
        for _ in range(k):
            val = 0
            for b in range(31):
                if bit_count[b] > 0:
                    val |= (1 << b)
                    bit_count[b] -= 1
            ans = (ans + val * val) % MOD

        return ans