class Solution:
    def subsetXORSum(self, nums):
        ans = 0
        n = len(nums)

        def dfs(i, cur):
            nonlocal ans

            if i == n:
                ans += cur
                return

            dfs(i + 1, cur)
            dfs(i + 1, cur ^ nums[i])

        dfs(0, 0)
        return ans