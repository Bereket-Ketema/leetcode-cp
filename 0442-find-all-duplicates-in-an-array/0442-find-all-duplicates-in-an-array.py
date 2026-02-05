class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        store = []
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == nums[r]:
                store.append(nums[l])
            l += 1; r += 1
        return store
                