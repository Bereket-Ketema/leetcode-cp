from typing import List
import math

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 1_000_000_007

        def count(arr: List[int]) -> int:
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            total_comb = math.comb(len(left) + len(right), len(left)) % MOD
            return (total_comb * count(left) * count(right)) % MOD

        return (count(nums) - 1) % MOD