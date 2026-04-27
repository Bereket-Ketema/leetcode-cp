class Solution:
    def isIdealPermutation(self, nums):
        return all(abs(nums[i] - i) <= 1 for i in range(len(nums)))