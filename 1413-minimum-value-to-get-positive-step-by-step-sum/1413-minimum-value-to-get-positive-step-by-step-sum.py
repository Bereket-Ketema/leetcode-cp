class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]

        return 1 if min(nums) >= 0 else 1 - min(nums)