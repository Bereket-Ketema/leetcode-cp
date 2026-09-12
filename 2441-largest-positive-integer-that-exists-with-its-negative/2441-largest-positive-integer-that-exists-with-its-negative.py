class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        store = set(nums)

        for i in range(len(nums)):
            negative = nums[i] - 2 * nums[i]

            if negative in store:
                return nums[i]
        
        return -1