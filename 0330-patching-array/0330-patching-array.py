class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        min_number, max_number, i = 0, 0, 0
        while max_number < n:
            if i < len(nums) and max_number + 1 >= nums[i]:
                max_number += nums[i]
                i += 1
            else:
                min_number += 1
                max_number += (max_number + 1)
        return min_number
