class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(idx, current):
            ans.append(current[:])
            if idx == len(nums):
                return

            for j in range(idx, len(nums)):
                current.append(nums[j])
                backtrack(j + 1, current)
                current.pop()
        backtrack(0, [])
        return ans