class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        gap = 0
        for i in range(1, len(nums)):
            gap = max(nums[i]-nums[i-1], gap)
        
        return gap
        