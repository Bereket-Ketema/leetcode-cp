class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        abebe = nums.copy()
        nums.sort()
        if nums[-2] * 2 <= nums[-1]:
            return abebe.index(nums[-1])
        else:
            return -1