class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = nums[0]
        for i in range(1,len(nums)):
            total += nums[i]
            nums[i] = total
        return nums