class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if len(nums1) == 1:
            return True

        has_even = any(x % 2 == 0 for x in nums1)
        has_odd = any(x % 2 == 1 for x in nums1)

        return has_even or has_odd