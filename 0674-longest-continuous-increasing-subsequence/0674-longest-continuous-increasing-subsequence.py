class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        store = 0
        check = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                check += 1
            else:
                store = max(store, check)
                check = 1
        store = max(store, check)
        return store