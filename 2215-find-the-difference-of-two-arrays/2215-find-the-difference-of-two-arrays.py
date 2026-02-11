class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        intr = nums1 & nums2
        return [list(nums1-intr),list(nums2-intr)]