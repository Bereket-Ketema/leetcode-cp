from math import comb

class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            leftWays = dfs(left)
            rightWays = dfs(right)

            return (
                comb(len(left) + len(right), len(left))
                * leftWays
                * rightWays
            ) % MOD

        return (dfs(nums) - 1) % MOD